def square_odds(values):
    numeros = values.split(",")
    numeros = [(int(i)) for i in numeros]
    res = [e**2 for e in numeros if e%2 != 0]
    res = [(str(i)) for i in res]
    return ",".join(res)
print(square_odds('1,2,3,4,5,6,7,8,9'))