num = int(input("Num: "))

lista = []

while num != 0:
    resto = int(num%10)
    num = int(num / 10)
    lista.append(resto)

if lista[0] == 0:
    lista.remove(lista[0])
    print(*lista, sep="")
else:
    print(*lista, sep="")