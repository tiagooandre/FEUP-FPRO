def sum_numbers(n):
    sum_n = 0
    for i in range(1, n+1):
        sum_n += i
    return sum_n
print(sum_numbers(100))