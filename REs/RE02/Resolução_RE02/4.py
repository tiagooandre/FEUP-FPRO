p = float(input("P: "))
n = float(input("n: "))
r = float(input("r: "))
t = 2

a = p * ((1 + (r / n)) ** (n * t))

print(round(a, 3))