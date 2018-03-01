from typing import List,Type
from math import *
from Ride import *
from Point import *
class Vehicule:


    def __init__(self, position: Point , rides: List[Ride]) -> None:
        self.position = position
        self.rides = rides
        self.isActive = False

    # Plus le score est proche de zero, plus il est bon
    def score(currentStep: int, ride: Ride) -> int:
        distance = math.fabs(self.position.r - ride.startPoint.r) + math.fabs(self.position.c - ride.startPoint.c)
        earliestStart = math.min(0, ride.earliestTime - currentStep)
        return distance + earliestStart

    def sortRidesByScore(currentStep : int, rides : List[Ride]) -> List[Ride]:
        return sorted(rides, key=lambda ride:self.score(currentStep,ride))

