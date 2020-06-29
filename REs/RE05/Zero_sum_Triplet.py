def triplet(atuple):

    res = ""
    newtuple = ()

    if (len(atuple) < 3):
        res = False
    else:
        for i in range(len(atuple)):
            for j in range(len(atuple)):
                if i == j:
                    continue
                else:
                    for k in range(len(atuple)):
                        if i == k and j == k:
                            continue
                        else:
                            if atuple[j] + atuple[k] == -atuple[i]:
                                newtuple = (atuple[k], atuple[j], atuple[i])

        res = newtuple
    return res

print(triplet((-1, 1, 1, 1)))