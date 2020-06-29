num = int(input("Num: "))
sum = 0

for i in range(1, num+1, 1):
    if (num % i == 0):
        sum += i

print(sum)