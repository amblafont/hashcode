# Usage : python3 executeFile.py fichier.in
from readInput import inputFileToProblem
from outputProblem import problemToStdOut
import sys

def executeFile(file : str):
    pb = inputFileToProblem(file)
    pb.LaunchSimulation()
    print(pb.score())
    #problemToStdOut(pb)

executeFile(sys.argv[1])


