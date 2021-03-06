from typing import List
from Map import *
from Vehicule import *
from Point import *
import sys
import Ride
class Problem:
    def score(self) -> int:
        score = 0
        for vehicule in self.vehicules:
            for ride in vehicule.rides:
                score += 1
                if ride.accessedTime <= ride.earliestTime:
                    score += self.bonus
        return score


    def __init__(self, map:Map, nbVehicules:int, rides : List[Ride.Ride], maxTime : int, bonus:int) -> None:
        self.currentStep = 0
        self.map = map
        self.vehicules = [ Vehicule(Point(0,0), []) for i in range(nbVehicules)]
        self.rides = rides
        self.maxTime = maxTime
        self.bonus = bonus

    def LaunchSimulation(self) -> None:
        while (self.currentStep < self.maxTime and self.rides):
            self.MapVehiculesRides()
            self.MakeVehiculesMove()
            self.currentStep += 1
            #print(" self.rides longueur: " + str(len(self.rides)), end='')
            #sys.stdout.flush()
            #print()
        
    def GetInactiveVehicules(self) -> List[Vehicule]:
        inactiveVehicules = []
        for vehicule in self.vehicules:
            if (not vehicule.isMoving):
                inactiveVehicules.append(vehicule)
        return inactiveVehicules

    

    def MapVehiculesRides(self) -> List[Vehicule]:
        for i in range(len(self.rides), 0):
            if ExcludeTooLongRide(self.rides[i], self.currentStep):
                self.rides[i].status = RideStatus.unavailable
                self.rides.remove(rides[i])

        vehicules = self.GetInactiveVehicules()
        for vehicule in vehicules:
            vehicule.updateRidesByScore(self.currentStep, self.rides)

        sortedVehicules = sortVehiculesByRidesWithScore(vehicules)
        for vehicule in sortedVehicules:
            for rideWithScore in vehicule.sortedRidesWithScores:
                if rideWithScore[0].status == RideStatus.available:
                    rideWithScore[0].status = RideStatus.unavailable
                    self.rides.remove(rideWithScore[0])
                    if (not ExcludeTooLongRide(rideWithScore[0], rideWithScore[1] + self.currentStep)):
                        rideWithScore[0].status = RideStatus.unavailable
                        vehicule.rides.append(rideWithScore[0])
                        rideWithScore[0].accessedTime = self.currentStep
                        vehicule.isMoving = True
                        
                        break
        return sortedVehicules

    def MakeVehiculesMove(self) -> None: 
        for vehicule in self.vehicules:
            # la voiture bouge et a au moins un trajet attribuée
            if vehicule.isMoving and vehicule.rides:
                # dernier trajet attribué à la voiture
                ride = vehicule.rides[-1]

                # la voiture se dirige vers le point de départ du trajet
                if not vehicule.isOnARide:
                    # la voiture est sur le point de départ
                    if vehicule.position == ride.startPoint:
                        # la voiture prend en charge le trajet
                        if self.currentStep - ride.earliestTime >= 0: 
                            vehicule.isOnARide = True
                        # la voiture attend
                        else:
                            pass
                    # la voiture se dirige vers le point de départ
                    elif vehicule.position.r > ride.startPoint.r: 
                        vehicule.position.r -= 1 
                    elif vehicule.position.r < ride.startPoint.r: 
                        vehicule.position.r += 1 
                    elif vehicule.position.c > ride.startPoint.c: 
                        vehicule.position.c -= 1 
                    elif vehicule.position.c < ride.startPoint.c: 
                        vehicule.position.c +=1 
 
                # la voiture se dirige vers le point d'arrivée du trajet
                if vehicule.isOnARide:
                    # la voiture se déplace jusqu'au point d'arrivée
                    if vehicule.position.r > ride.finishPoint.r: 
                        vehicule.position.r -= 1
                    elif vehicule.position.r < ride.finishPoint.r: 
                        vehicule.position.r += 1 
                    elif vehicule.position.c > ride.finishPoint.c: 
                        vehicule.position.c -= 1 
                    elif vehicule.position.c < ride.finishPoint.c: 
                        vehicule.position.c +=1 
                    else: 
                        vehicule.isMoving = False

