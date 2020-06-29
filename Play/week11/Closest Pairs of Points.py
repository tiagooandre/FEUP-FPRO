def distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def calculate(alist, min_dist = 9999999999):
    for x1, y1 in alist:
        for x2, y2 in alist:
            if abs(x2 - x1) < min_dist:
                dist = distance((x1, y1), (x2, y2))
                min_dist = dist if (dist != 0 and dist < min_dist) else min_dist
    return round(min_dist)


def closest_pair(points):
    return (calculate(sorted(points)))