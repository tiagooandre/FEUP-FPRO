def fib(n):
    lista = [0, 1]
    if n == 0 or n == 1:
        return [0]
    else:
        for i in range(2, n):
            lista.append(lista[i-2]+lista[i-1])

    return lista

print(fib(13))