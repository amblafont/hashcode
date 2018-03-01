from typing import TypeVar, Generic
import Point
class Ride:


    def __init__(self, startPoint: Point , finishPoint: Point, earliestTime, latestTime) -> None:
        self.startPoint = startPoint
        self.finishPoint = finishPoint
        self.earliestTime = earliestTime
        self.latestTime = latestTime
