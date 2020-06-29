def repeated_letter(s):
    count = 0

    for i, c in enumerate(s):
        for j in s[i+1:]:
            if c == j:
                return c
    return None

print(repeated_letter("tweet"))