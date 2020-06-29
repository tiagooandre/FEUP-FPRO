n = float(input("N: "))

mid = float(n / 2)

lim_inf = 0
lim_sup = n

while abs(mid*mid - n) > 0.00001:
    if mid*mid > n:
        lim_sup = mid
    if mid*mid < n:
        lim_inf = mid
    lim_inf += 0.00000001
    lim_sup -= 0.00000001

    mid = (lim_sup + lim_inf)/2.0

print(round(mid, 5))