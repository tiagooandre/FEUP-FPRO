def collisions(alist):
    res = {}
    for i in alist:
        h = sum(map(int, str(i))) % 8
        res[h] = res.get(h, 0) + 1

    return res

print(collisions([24, 42]))