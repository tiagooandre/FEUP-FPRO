def to_celsius(t):
    res = [round((x-32)/1.8, 1) for x in t]
    return res
print(to_celsius([84.56, 79.7, 81.14, 82.4, 82.04]))