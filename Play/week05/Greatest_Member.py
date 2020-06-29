def size(string):
    res = 0
    for i in string:
        res += ord(i)
    return res


def foo(atuple):
    res = 0
    for i in atuple:
        if isinstance(i, tuple):
            foo(i)
        else:
            res += size(i)
    return res


def greatest_member(atuple):
    if len(atuple) == 0:
        return ()
    highest = ("", 0)
    for i in atuple:
        if isinstance(i, str):
            if highest[1] < size(i):
                highest = (i, size(i))
        if isinstance(i, tuple):
            if highest[1] < foo(i):
                highest = (i, foo(i))

    return highest[0]

print(greatest_member(('hyde', 'jekyll')))