from math import dist
g = lambda: tuple(map(int, input().split()))
N = int(input())
p = [g() for _ in range(N)]
x, y = map(sum, zip(*p))
print(x, y)
print("%.2f" % min(dist((x, y), q) for q in p))