from typing import List
import Map,Ride,Vehicule
class Problem:

    self.currentStep = 0

    def __init__(self, map:Map, nbVehicules:int, rides : List[Ride.Ride], maxTime : int, bonus:int) -> None:
        self.map = map
        self.vehicules = [ Vehicule(Point(0,0), []) for i in range(nbVehicules)]
        self.rides = Rides
        self.maxTime = maxTime
        self.bonus = bonus
