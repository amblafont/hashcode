from enum import Enum

class RideStatus(Enum):
    available = 1
    ongoing = 2
    skipped = 3
    finished = 4