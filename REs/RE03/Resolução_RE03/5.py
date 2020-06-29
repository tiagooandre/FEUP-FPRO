num = int(input("Num: "))

x1 = num / 2.0
x2 = x1 + 1

while (x1 != x2):
    n = num / x1
    x2 = x1
    x1 = round((x1 + n)/2, 2)

print(x1)