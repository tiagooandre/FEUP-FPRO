def brute_force(f, l):
    return list(filter(f, [x+y+z for x in l for y in l for z in l]))
print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))