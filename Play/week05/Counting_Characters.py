def count_chars(astring):
    count_d = 0
    count_s = 0
    count_a = 0
    for i in astring:
        if i.isdigit():
            count_d += 1
        elif i.isalpha():
            count_a += 1
        else:
            count_s += 1

    return (count_a, count_d, count_s)

print(count_chars("Str1nG$"))