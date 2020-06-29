def rearrange(l):
    return list(filter(lambda x: x <= 0, l)) + list(filter(lambda x: x > 0, l))
print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))