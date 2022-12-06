n, i, count = int(input()), 1, 0
while n > 0:
    if n >= i:
        n, i = n - i, i + 1
    else:
        n, i = n - 1, 2
    count += 1
print(count)