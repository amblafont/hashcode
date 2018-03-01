
from Problem import *
from Ride import *
from Point import *

def inputFileToProblem (pb : Problem) -> None:
    with open(file) as f:
        nbRows,nbCols, nbVehicules, nbRides, bonus, maximumTime = f.readline().split()
        rides = []
        for line in f:
            print(line)
            a,b,x,y,s,fin = line.split()
            startPoint = Point.Point(a,b)
            finishPoint = Point.Point(x,y)
            rides.append(Ride(startPoint, finishPoint, s, fin))
        map = Map(nbRows, nbCols)
        return Problem(map, nbVehicules, rides, maximumTime)
