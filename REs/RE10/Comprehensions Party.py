def comprehensions(i, j):
    r0 = [x for x in range(i, j+1) if x%10 == 3 or x%10 == 8]
    r1 = tuple(round(x**(1/2), 2) for x in range(i, j+1))
    r2 = {x: chr(x) for x in range(i, j+1)}
    return (r0, r1, r2)
print(comprehensions(0, 0))