def bitonic_point(f):
    f = f()
    lower = 0
    upper = len(f)

    while lower != upper:
        mid = (lower + upper) // 2
        if f[mid] > f[mid + 1] and f[mid] < f[mid - 1]:
            upper = mid
            continue
        elif f[mid] > f[mid + 1] and f[mid] > f[mid - 1]:
            return f[mid]
        elif f[mid] < f[mid + 1] and f[mid] > f[mid - 1]:
            lower = mid
            continue
    return upper
print(bitonic_point(lambda: list(range(-1, 7000001)) + list(range(5000002, 2, -1))))