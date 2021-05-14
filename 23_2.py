from math import pi

def find_farthest_orbit(orbits):
    orbmax = None
    max_s = 0
    for a, b in orbits:
        if a*b*pi > max_s and a != b:
            max_s = a*b*pi
            orbmax = (a, b)
    return orbmax