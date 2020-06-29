def last_man_standing(alist, step):
    i = 0
    while (len(alist) != 1):
        i = (i+step-1) % len(alist)
        del alist[i]

    return alist[0]

print(last_man_standing(['Andre', 'Rui', 'Silva', 'Madalena', 'Leonor', 'Francisco', 'Filomena'], 7))