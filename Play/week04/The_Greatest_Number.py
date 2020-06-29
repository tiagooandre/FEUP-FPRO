def greatest(num):
    string = str(num)
    lista = []
    for i in string:
        lista += i

    lista.sort(reverse=True)
    return(int("".join(lista)))

print(greatest(310909))