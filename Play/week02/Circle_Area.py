import math

def circle(r):
    #r = float(input("Radius: "))
    area = math.pi * r ** 2
    return round(area, 2)
    #round(___, ___) -> variavel e n. de casa decimais a arredondar
print(circle(2))