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
    	for vehicule in vehicules:
    		vehicule.updateRidesByScore(self.currentStep, self.rides)

    	sortedVehicules = sortVehiculesByRidesWithScore(vehicules)
    	for vehicule in sortedVehicules:
    		for rideWithScore in vehicule.sortedRidesWithScores:
    			if rideWithScore[0].status == RideStatus.available:
    				rideWithScore[0].status = RideStatus.ongoing
    				vehicule.rides.append(rideWithScore[0])
    				vehicule.isActive = True
    				break

    def MakeVehiculesMove(self) -> None:
        return

