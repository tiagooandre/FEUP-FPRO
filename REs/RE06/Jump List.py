def jump(l):
    i = 0
    sum = 0
    while l[i] != -1:
        i = l[i]
        sum += 1

    return sum

print(jump([6, 8, 4, 7, -1, 1, 2, -1, 3]))