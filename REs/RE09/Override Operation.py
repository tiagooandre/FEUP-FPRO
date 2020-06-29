def override(l1, l2):
    i = list(map(lambda x: x[0], l2))
    l = filter(lambda x: x[0] not in i, l1)
    return sorted(list(l) + l2, key = lambda x: x[0])
print(override([('c', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'd')], [('a', 'c'), ('b', 'd')]))