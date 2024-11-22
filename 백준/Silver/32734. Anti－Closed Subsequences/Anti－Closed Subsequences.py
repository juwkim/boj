input()
for num in map(int, input().split()):
    i, d = 0, 1
    while num % (d << 1) != d:
        i += 1
        d <<= 1
    print(i + 1, end=' ')