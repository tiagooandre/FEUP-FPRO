def pattern_hunting(l1, l2, p):
    lista_final = []
    for i in range(len(l1)):
        if p in l1[i]:
            lista_final.append(l2[i])
        if p in l2[i]:
            lista_final.append(l1[i])
    lista_final.sort(reverse=True)

    return lista_final

print(pattern_hunting(['a string', 'two strings', 'not here'], ['choose me', 'me too', 'but not me'], 'string'))