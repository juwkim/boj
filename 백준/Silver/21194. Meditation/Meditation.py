g = lambda: [*map(int, input().split())]

n, k = g()
print(sum(sorted([int(input()) for _ in range(n)])[-k:]))