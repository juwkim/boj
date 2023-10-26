n = int(input())
for i, j in zip(range(1, n + 1), range(n, 0, -1)):
    print(i * j)