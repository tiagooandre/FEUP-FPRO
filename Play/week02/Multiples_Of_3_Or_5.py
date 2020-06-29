def sum_multiples(n):
    #n = int(input("Number: "))
    i = 0
    sum = 0

    for i in range(0, n+1, 1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum;
print(sum_multiples(5))