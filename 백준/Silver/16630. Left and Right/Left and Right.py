n, i = int(input()), 0
for c in input().split('R'):
    i += len(c) + 1
    print(*range(i, i - len(c) - 1, -1))