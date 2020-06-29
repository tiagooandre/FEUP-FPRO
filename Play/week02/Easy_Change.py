import math

price = float(input("Price: "))
received = int(input("Amount Received: "))

money = received - price
aux1 = 0
aux_1 = 0
aux2 = 0
aux_2 = 0
aux3 = 0
aux_3 = 0
aux4 = 0
aux_4 = 0

if (money/50) >= 1:
    aux1 = int(money/50) #3,1
    aux_1 = aux1 * 50 #150
    money -= aux_1 #155-150=5

if (money/20) >= 1:
    aux2 = int(money/20)
    aux_2 = aux2 * 20
    money -= aux_2

if (money/10) >= 1:
    aux3 = int(money/10)
    aux_3 = aux3 * 10
    money -= aux_3

if (money/5) >= 1:
    aux4 = int(money/5)
    aux_4 = aux4 * 5
    money -= aux_4

res = str(aux1) + " " + str(aux2) + " " + str(aux3) + " " + str(aux4)
print(res)