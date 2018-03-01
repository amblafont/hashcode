from typing import List
import Map,Ride,Vehicule
class Problem:


    def __init__(self, map:Map, nbVehicules:int, rides : List[Ride.Ride]) -> None:
        self.map = map
        self.vehicules = [ Vehicule(Point(0,0), []) for i in range(nbVehicules)]
        self.rides = Rides
