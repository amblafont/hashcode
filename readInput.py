
import Problem,Ride

def inputFileToProblem (file : str) -> Problem:
    with open(file) as f:
        nbRows,nbCols, nbVehicules, nbRides, bonus, maximumTime = f.readline().split()
        rides = []
        for line in f:
            a,b,x,y,s,f = line
            startPoint = Point(a,b)
            finishPoint = Point(x,y)
            rides.append(Ride(startPoint, finishPoint, s, f))
        map = Map(nbRows, nbCols)
        return Problem(map, nbVehicules, rides, maximumTime)

