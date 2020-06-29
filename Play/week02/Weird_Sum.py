a = int(input("A: "))
b = int(input("B: "))

sum = 0
prod = 0

while (a-b)% 2 == 0:
    sum = a + b
    sum *= 2
    break

while (a-b) % 2 != 0:
    prod = a * b
    sum = a+b+prod
    break;

print(sum)