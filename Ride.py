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
