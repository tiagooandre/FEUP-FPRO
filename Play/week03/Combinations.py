def C(n, r):
    sum_n = 1
    sum_r = 1

    for i in range(n, 0, -1):
        sum_n *= i

    for i in range(r, 0, -1):
        sum_r *= i

    x = n - r
    sum_x = 1

    for i in range(x, 0, -1):
        sum_x *= i

    c = (sum_n / (sum_r * sum_x))

    return int(c)
print(C(6, 2))