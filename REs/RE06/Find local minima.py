def local_minima(alist, n):
    l_min = []
    for inter, x in enumerate(alist):
        neighbor = [alist[i] for i in range(inter-n//2, inter+n//2+1) if i in range(len(alist)) and i != inter]
        if all(x <= y for y in neighbor):
            if not any (x == y and (y, j) in l_min for j in range(inter-n//2, inter) for y in neighbor):
                l_min.append(x, inter)

    return l_min