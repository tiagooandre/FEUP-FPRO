num = int(input("Num: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(False)
            break
    else:
        print(True)