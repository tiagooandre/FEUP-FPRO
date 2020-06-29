def get_composites(n):
    for i in range(n+1):
        for j in range(2, i):
            if i % j == 0:
                yield i
                break
print(get_composites([4]))