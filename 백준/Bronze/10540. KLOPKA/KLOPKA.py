x, y = zip(*[[*map(int, input().split())] for _ in range(int(input()))])
print(max(max(x) - min(x), max(y) - min(y))**2)