def no_consecutives1(k):
    return len([bin(x) for x in range (0, 2**k) if "11" not in str(bin(x))])