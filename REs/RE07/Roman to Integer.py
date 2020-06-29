def roman_to_integer(astring):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    soma = 0
    for i in range(len(astring)-1):
        if roman[astring[i]] >= roman[astring[i+1]]:
            soma += roman[astring[i]]
        else:
            soma -= roman[astring[i]]
    soma += roman[astring[-1]]

    return soma

print(roman_to_integer("MMMCMXCIX"))