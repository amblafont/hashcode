
from Problem import *
from Ride import *
from Point import *

def problemToStdOut (pb : Problem) -> None:
    for vehicule in pb.vehicules:
        print(len(vehicule.rides), end='')
        for ride in vehicule.rides: 
            print(" " + str(ride.number), end='')
        print()


