def bagdiff(xs, ys):
    l = []
    for i in xs:
        for j in ys:
            if i == j:
                xs.remove(i)
                ys.remove(j)

    return xs

print(bagdiff([5, 7, 11, 11, 11, 12, 13], [7, 8, 11]))