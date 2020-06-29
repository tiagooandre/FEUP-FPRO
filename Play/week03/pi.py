import math

pi = 0

calc = ((2*math.sqrt(2))/9801)

i = 0
aux = 0

for i in range (0, 50, 1):
    aux += (math.factorial(4*i)*(1103+26390*i))/(math.factorial(i)**4*396**(4*i))

final = round(1/(calc * aux), 8)

print(final)