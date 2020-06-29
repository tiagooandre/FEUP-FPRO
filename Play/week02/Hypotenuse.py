from math import sqrt

def hypotenuse(n):
    #n = int(input("N Length: "))
    hyp = round(sqrt(n**2 + n**2), 2)
    return hyp
print(hypotenuse(2))