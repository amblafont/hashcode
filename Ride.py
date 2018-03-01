from typing import TypeVar, Generic
import Point, RideStatus
class Ride:

    def __init__(self, startPoint: Point , finishPoint: Point, earliestTime, latestTime) -> None:
        self.startPoint = startPoint
        self.finishPoint = finishPoint
        self.earliestTime = earliestTime
        self.latestTime = latestTime
        self.status = RideStatus.available

    def setStatus (status: RideStatus) -> None:
        self.status = status