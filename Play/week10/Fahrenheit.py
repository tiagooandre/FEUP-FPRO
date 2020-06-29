def to_fahrenheit(t):
    res = [round((x*1.8)+32, 2) for x in t]
    return res
print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))