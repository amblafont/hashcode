from readInput import inputFileToProblem
from outputProblem import problemToStdOut
from inputFileNames import *



pb = inputFileToProblem(FILE_1)
print(pb.MapVehiculesRides())
problemToStdOut(pb)

