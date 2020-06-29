def collatz(n):
    collatz_num = str(n)

    while (n != 1):
        if (n % 2) == 0:
            n = n // 2
            collatz_num += "," + str(n)
        else:
            n = n * 3 + 1
            collatz_num += "," + str(n)

    return collatz_num
print(collatz(3))