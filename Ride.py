from typing import TypeVar, Generic
from Point import *
from RideStatus import *
class Ride:

    def __init__(self, startPoint: Point , finishPoint: Point, earliestTime : int, latestTime : int, number : int) -> None:
        self.startPoint = startPoint
        self.finishPoint = finishPoint
        self.earliestTime = earliestTime
        self.latestTime = latestTime
        self.status = RideStatus.available
        self.number = number
        self.length = abs(self.startPoint.r - self.finishPoint.r) + abs(self.startPoint.c - self.finishPoint.c)

def ExcludeTooLongRide(ride: Ride, totalDistance:int) -> None:
	return ride.latestTime <= ride.length + totalDistance
