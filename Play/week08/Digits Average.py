import math
def my_while(n2, r, p, n):
    if n < 10:
        return r
    n2 = n//10
    r += (math.ceil((n2%10 + n%10)/2))*p
    return my_while(n2, r, p*10, n//10)

def digits_average(n):
    if(n<10):
        return n
    return digits_average(my_while(n, 0, 1, n))