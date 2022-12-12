from math import dist
p = [tuple(map(int, input().split())) for _ in range(int(input()))]
x, y = map(sum, zip(*p))
print(x, y)
print("%.2f" % min(dist((x, y), q) for q in p))