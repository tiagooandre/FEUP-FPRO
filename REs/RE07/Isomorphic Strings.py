def isomorphic(astring1, astring2):
    counter = 0
    res = []
    dict = {}
    diff1 = []
    diff2 = []

    for char1 in astring1:
        if char1 not in diff1:
            diff1.append(char1)

    for char2 in astring2:
        if char2 not in diff2:
            diff2.append(char2)

    if len(diff1) != len(diff2):
        return "'" + astring1 + "'" + " and " + "'" + astring2 + "'" + " are not isomorphic"

    for char in astring1:
        dict[char] = astring2[counter]
        counter += 1

    for element in dict:
        res.append((element, dict[element]))

    return "'" + astring1 + "'" + " and " + "'" + astring2 + "'" + " are isomorphic because we can map: " + str(res)

print(isomorphic('paper', 'title'))