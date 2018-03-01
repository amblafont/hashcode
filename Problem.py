from typing import List
from Map import *
from Vehicule import *
from Point import *
import Ride
class Problem:


    def __init__(self, map:Map, nbVehicules:int, rides : List[Ride.Ride], maxTime : int, bonus:int) -> None:
        self.currentStep = 0
        self.map = map
        self.vehicules = [ Vehicule(Point(0,0), []) for i in range(nbVehicules)]
        self.rides = rides
        self.maxTime = maxTime
        self.bonus = bonus

    def LaunchSimulation(self) -> None:
        MapVehiculesRides()
        MakeVehiculesMove()
        

    def GetInactiveVehicules(self) -> List[Vehicule]:
    	inactiveVehicules = []
    	for vehicule in self.vehicules:
    		if (not vehicule.isActive):
    			inactiveVehicules.append(vehicule)
    	return inactiveVehicules

    def MapVehiculesRides(self) -> None:
    	for i in range(len(self.rides, 0)):
    		if self.rides[i].status != RideStatus.available:
    			self.rides.remove(ride)

    	vehicules = GetInactiveVehicules()

    	sortedVehicules = [ [] for i in range(self.map.nbRows + self.map.nbColumns) ]
    	for vehicule in vehicules:
    		sortedVehicules[vehicule.sortedRidesWithScores[0][1]].append(vehicule)

    def MakeVehiculesMove(self) -> None: 
        for vehicule in self.vehicules:
            # la voiture a au moins un trajet attribuée
            if vehicule.rides:
                # dernier trajet attribué à la voiture
                ride = vehicule.rides[-1] 
                         
                # le trajet est disponible
                if ride.available:
                    # la voiture est sur le point de départ
                    if vehicule.position == ride.startPoint:
                        # la voiture prend en charge le trajet
                        if self.currentStep - ride.earliestTime >= 0: 
                            vehicule.isActive = True
                        # la voiture attend
                        else:
                            pass
                    # la voiture se dirige vers le point d'arrivée
                    else:
                        if vehicule.position.r > ride.finishPoint.r: 
                            vehicule.position.r -= 1 
                        elif vehicule.position.r < ride.finishPoint.r: 
                            vehicule.position.r += 1 
                        elif vehicule.position.c > ride.finishPoint.c: 
                            vehicule.position.c -= 1 
                        elif vehicule.position.c < ride.finishPoint.c: 
                            vehicule.position.c +=1 
                        else: 
                            vehicule.isActive = False
 
                # la voiture se déplace le long du trajet jusqu'au point d'arrivée
                if vehicule.isActive: 
                    if vehicule.position.r > ride.finishPoint.r: 
                        vehicule.position.r -= 1 
                    elif vehicule.position.r < ride.finishPoint.r: 
                        vehicule.position.r += 1 
                    elif vehicule.position.c > ride.finishPoint.c: 
                        vehicule.position.c -= 1 
                    elif vehicule.position.c < ride.finishPoint.c: 
                        vehicule.position.c +=1 
                    else: 
                        vehicule.isActive = False

