from functools import reduce

def map_reduce(n1, n2):
    i = [n*n for n in range(n1, n2) if n%2 == 1]
    return reduce(lambda x, y: x*y if x*y < 50 else x+y, i)
print(map_reduce(0, 5))