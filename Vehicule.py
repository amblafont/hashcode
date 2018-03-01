from typing import List,Type
from math import *
from Ride import *
from Point import *
class Vehicule:


    def __init__(self, position: Point , rides: List[Ride]) -> None:
        self.position = position
        self.rides = rides
        self.isMoving = False
        self.isOnARide = False

    # Plus le score est proche de zero, plus il est bon
    def score(self, currentStep: int, ride: Ride) -> int:
        distance = math.fabs(self.position.r - ride.startPoint.r) + math.fabs(self.position.c - ride.startPoint.c)
        earliestStart = math.min(0, ride.earliestTime - currentStep)
        return distance + earliestStart

    def sortRidesByScore(self, currentStep : int, rides : List[Ride]):
        ridesWithScore = [(ride, self.score(currentStep, ride)) for ride in rides]
        return sorted(ridesWithScore, key=lambda rideWithScore:rideWithScore[1])
    def updateRidesByScore(self, currentStep : int, rides : List[Ride]) -> None:
        self.sortedRidesWithScores = self.sortRidesByScore(currentStep, rides)


# TODO vérifier que le truc sortedRidesWithScore est non vide
def sortVehiculesByRidesWithScore(vehicules : List[Vehicule]) -> List[Vehicule]:
    return sorted(vehicules, key = lambda vehicule: [rideWithScore[1] for rideWithScore in vehicule.sortedRidesWithScores ])



