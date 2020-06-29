def treasure(clues):
    i = (0, 0)
    while i in clues:
        y = clues[i]
        del clues[i]
        i = y
    return i

print(treasure({(0, 0): (1, 0), (2, 1): (3, 5), (1, 0): (2, 1)}))