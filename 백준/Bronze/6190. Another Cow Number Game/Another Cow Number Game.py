N = int(input())
count = 0
while N != 1:
    count += 1
    if N % 2:
        N = 3 * N + 1
    else:
        N //= 2
print(count)