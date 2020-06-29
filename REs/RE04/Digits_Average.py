def digits_average(n):

    if n < 10:
        return n

    n1 = n % 10
    exp = 0
    res = 0

    while n >= 10:
        n = n // 10
        res += int((n % 10 + n1 + 1) / 2) * 10 ** exp
        n1 = n % 10
        exp += 1
    return digits_average(res)

print(digits_average(3434))