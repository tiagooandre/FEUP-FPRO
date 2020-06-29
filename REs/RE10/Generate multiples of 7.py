def multiples_of7(n):
    mult = (multi for multi in range(0, n) if multi%7 == 0)
    return mult
print(multiples_of7(21))