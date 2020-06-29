def is_perfect(n):
    count = 0
    for i in range(1, n):
        if (n % i) == 0:
            count += i

    if count == n:
        return True
    else:
        return False

print(is_perfect(60))