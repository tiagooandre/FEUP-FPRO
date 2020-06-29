def adigits(str1, str2, str3):

    lista = []
    lista += str1 + str2 + str3
    lista.sort(reverse=True)

    return("".join(lista))

print(adigits("1", "0", "1"))