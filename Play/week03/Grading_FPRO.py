import math

LE = float(input("LE: "))
RE = float(input("RE: "))
PE = float(input("PE: "))
TE = float(input("TE: "))

grade = (LE + RE + 5 * PE + 3 * TE) / 50

if (LE < 0 or LE > 100) or (RE < 0 or RE > 100) or (PE < 0 or PE > 100) or (TE < 0 or TE > 100):
    print("Input error")
elif (PE < 40 or TE < 40):
    print("RFC")
else:
    print(int(grade + 0.5))