n = int(input())
x, y = zip(*[[*map(int, input().split())] for _ in range(n)])
print(sum(abs(x[i - 1] - x[i]) + abs(y[i - 1] - y[i]) for i in range(n)) - 2 * (max(x) - min(x) + max(y) - min(y)))