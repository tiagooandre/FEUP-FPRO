def nth_lowest(lnum, n):
    new_list = []
    new_list = lnum.sort()

    return lnum[n-1]

print(nth_lowest([42, 234, 135, 21, 232, 12312, -2343], 2))