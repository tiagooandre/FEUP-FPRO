def evaluate(a, x):
    return sum([i * (x**(a.index(i))) for i in a])
print(evaluate([1, 2, 4], 5))