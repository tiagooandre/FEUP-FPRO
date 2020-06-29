def gcd_rec(n1, n2):

    res = n1 % n2

    if res:
        return gcd_rec(n2, res)

    return n2

print(gcd_rec(12, 14))