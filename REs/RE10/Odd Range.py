def odd_range(start, stop, step):
    for i in range(start+(1*start%2==0), stop, 2*step):
        yield i
print(odd_range(1, 10, 1))