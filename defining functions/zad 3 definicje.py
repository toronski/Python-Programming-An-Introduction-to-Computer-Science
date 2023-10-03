
from math import *

n = eval(input("Podaj ile wynosi promień kuli: "))

def sphereArea(radius):
    return 4 * pi * radius * 2

def sphereVolume(radius):
    return 4 / (3 * pi * radius ** 3)


print("Pole kuli wynosi " + str(sphereArea(n)))
print("Objętość kuli to: " + str(sphereVolume(n)))
