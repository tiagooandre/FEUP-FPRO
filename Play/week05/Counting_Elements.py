def count_until(tup):
    for i, c in enumerate(tup): #i dá-me index e o c o valor do index
        if type(c) == tuple:
            return i
    return -1

print(count_until((1, 2, (3,), 4.0, 5j)))