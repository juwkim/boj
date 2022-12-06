input()
n = [*map(int, input().split())]
start, size = n[0], 0
for x, y in zip(n, n[1:]):
    if x >= y:
        size = max(size, x - start)
        start = y
print(max(size, n[-1] - start))