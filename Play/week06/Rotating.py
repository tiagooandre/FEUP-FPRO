def rotate_list(l):
    l = l[3:] + l[:3]
    return l

print(rotate_list([1, 2, 3, 4, 5, 6]))