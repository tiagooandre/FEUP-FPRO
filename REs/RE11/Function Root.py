def bisect(f, n):
    lower = 0
    upper = 1
    for i in range(n):
        midpoint = (lower + upper) / 2.0
        if (f(midpoint) > 0 and f(lower) > 0) or (f(midpoint) < 0 and f(lower) < 0):
            lower = midpoint
        else:
            upper = midpoint
    return round(midpoint, 5)
print(bisect(lambda x: (1-(x+0.2))*(x+0.2), 10))