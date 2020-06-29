def palindrome_index(s):
    if len(s) == 0:
        return 0
    else:
        lista = list(s)
        if lista == lista[::-1]:
            return -1
        else:
            for i in range(len(s)):
                lista = list(s)
                lista.pop(i) #Retira o caracter do index i
                if lista == lista[::-1]:
                    return i
                else:
                    continue
            return -1

print(palindrome_index("aaab"))