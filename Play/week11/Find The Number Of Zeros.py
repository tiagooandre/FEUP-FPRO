def count_zeros(f):
    f = f()
    upper = len(f)
    lower = 0
    while True:
        mid = (lower+upper)//2
        if (f[mid] == 0) and (f[mid-1] == 1):
            return len(f)-(mid)
        if (f[mid] == 0) and (f[mid-1] == 0):
            upper = mid
        else:
            lower = mid
    return upper
print(count_zeros(lambda: [1]*80000000 + [0]*70000000))