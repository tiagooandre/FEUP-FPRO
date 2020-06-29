#Equilátero: Lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Nenhum lado igual

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a+b > c and a+c > b and b+c > a:
    if a == b and b == c or a == c and b == a or a == c and b == c:
        print("Equilateral")
    elif a == b and b != c or a == c and b != a:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a triangle")