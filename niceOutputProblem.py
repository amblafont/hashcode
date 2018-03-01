
from Problem import *
from Ride import *
from Point import *

import matplotlib.pyplot as plt


def problemToNiceGraph (pb : Problem) -> None:
    x = []
    y = []
    for vehicule in pb.vehicules:
        x.append(vehicule.position.c)
        y.append(vehicule.position.r)
    plt.scatter(x, y)
    plt.show()


