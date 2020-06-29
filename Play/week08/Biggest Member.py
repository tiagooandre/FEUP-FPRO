def biggest_member(atuple):
    if type(atuple) != tuple:
        return (atuple, )
    else:
        big = atuple
        for n in atuple:
            if isinstance(n, tuple):
                x = biggest_member(n)
                if len(x) > len(big):
                    big = x

        return big