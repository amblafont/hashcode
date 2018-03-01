
from Problem import *
from Ride import *
# from Point import *
from Map import *

def inputFileToProblem (file : str) -> Problem:
    with open(file) as f:
        nbRows,nbCols, nbVehicules, nbRides, bonus, maximumTime = [int(x) for x in f.readline().split()]
        rides = []
        rideNumber = 0
        for line in f:
            # print(line)
            a,b,x,y,s,fin = [int(x) for x in line.split()]
            startPoint = Point.Point(a,b)
            finishPoint = Point.Point(x,y)
            rides.append(Ride.Ride(startPoint, finishPoint, s, fin, rideNumber))
            rideNumber = rideNumber + 1
        map = Map(nbRows, nbCols)
        return Problem(map, nbVehicules, rides, maximumTime, bonus)

