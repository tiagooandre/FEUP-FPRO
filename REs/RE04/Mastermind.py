def count_points(g, k):
    points = 0
    for i in g:
        for j in k:
            if (i == j):
                if (g.index(i) == k.index(j)):
                    points += 3
                else:
                    points += 1
                g = g[:g.index(i)] + " " + g[g.index(i) + 1:]
                k = k[:k.index(j)] + " " + k[k.index(j) + 1:]
                break

    return points


def mastermind(g1, g2, g3, c1, c2, c3):
    guess = g1 + g2 + g3
    key = c1 + c2 + c3

    points = count_points(guess, key)

    return points

print(mastermind('b', 'w', 'y', 'b', 'w', 'y'))