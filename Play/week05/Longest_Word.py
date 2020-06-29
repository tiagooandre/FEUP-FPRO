def longest(s):
    words = s.split(" ")
    aux = 0

    for i in words:
        if len(i) > aux:
            aux = len(i)

    return aux
