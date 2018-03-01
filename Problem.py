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

    def MakeVehiculesMove() -> None:
        return

