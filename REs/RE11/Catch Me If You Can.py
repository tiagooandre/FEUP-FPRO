def find_me(f, limits):
    mid = (limits[0] + limits[1])//2
    if (f(mid) == 0):
        return 0
    if (f(mid) == -1):
        return 1 + find_me(f, (limits[0], mid))
    return 1 + find_me(f, (mid, limits[1]))
print(find_me(lambda n: -1 if n > 563 else 1 if n < 563 else 0, (-5000, 5000)))