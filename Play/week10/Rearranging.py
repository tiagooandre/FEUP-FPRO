def rearrange(l):
    negative = [i for i in l if i <= 0]
    positive = [i for i in l if i > 0]
    res = negative + positive
    return res
print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))