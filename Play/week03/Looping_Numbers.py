n = float(input("N: "))

res = int(n % 10)
n = int(n / 10)
n1 = int(res)

flag = True

if n < 10:
    flag = True
else:
    while n != 0:
        res = int(n % 10)
        n = int(n / 10)
        if abs(res - n1) != 1:
            flag = False
            break
        n1 = res

if flag:
    print("Looping number")
else:
    print("Not a looping number")