l = int(input("L: "))
s = int(input("S: "))

r = l
if r > s:
    while s <= r:
        r = r-s
        if s > r:
            if r != 0:
                l = r
                r = s
                s = l
else:
    l = r
    r = s
    s = l
    while s <= r:
        r = r-s
        if s > r:
            if r != 0:
                l = r
                r = s
                s = l
print(s)