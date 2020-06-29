d = int(input("d: "))
num = int(input("Num: "))

lista_greater = []

aux = 0
num_str = str(num)

for i in num_str:
    lista_greater.append(i)

for i in lista_greater:
    if int(d) < int(i):
        aux = int(aux) + int(i)*int(i)
        
print(aux)