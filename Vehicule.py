from typing import List,Type
import Point,Ride
class Vehicule:


    def __init__(self, position: Point , rides: List[Ride.Ride]) -> None:
        self.position = position
        self.rides = rides
