from readInput import inputFileToProblem
from outputProblem import problemToStdOut
from inputFileNames import *



pb = inputFileToProblem(FILE_1)
toto = pb.MapVehiculesRides()
print(str(toto[0].rides[0].startPoint.r) + " " +str(toto[0].rides[0].startPoint.c))
print(str(toto[1].rides[0].startPoint.r) + " " +str(toto[1].rides[0].startPoint.c))
problemToStdOut(pb)

