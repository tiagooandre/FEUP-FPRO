import math

def solver(a, b, c):

    quad = []

    if (b**2-4*a*c) > 0:
        quad = [(-b + math.sqrt(b**2-4*a*c))/(2*a), (-b - math.sqrt(b**2-4*a*c))/(2*a)]
        quad.sort()
        return quad
    elif (b**2-4*a*c) == 0:
        quad = [(-b / (2*a))]
        return quad
    else:
        return quad

print(solver(-2, -5, -3))