def palindrome(astring):
    count = 0
    for i in range(len(astring)):
        for j in range(i + 1, len(astring)):
            if astring[i] == astring[j]:
                new = astring[i:j + 1]
                if new == new[::-1]:
                    count += 1
                else:
                    count += 0
    return "The string 'geek' contains " + str(count) + " palindrome substrings."


print(palindrome('nope'))