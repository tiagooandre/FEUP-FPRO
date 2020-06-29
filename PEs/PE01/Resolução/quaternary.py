quat = int(input("Quat: "))

lista = []

res = [int(x) for x in str(quat)]
res1 = res[::-1]

count = 0

for i in range(0, len(res1)):
    count += res1[i] * (4**i)
    
print(count)