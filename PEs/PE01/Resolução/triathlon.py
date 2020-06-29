tS = float(input("Swimming: "))
tC = float(input("Cycling: "))
tR = float(input("Running: "))

total = tS + tC + tR

vS = 1.5/tS
vC = 40/tC
vR = 10/tR

if (tS + tC + tR > 4):
    print("Time")
elif vS < 2:
    print("Swimming")
elif vC < 20:
    print("Cycling")
elif vR < 8:
    print("Running")
else:
    print(total)