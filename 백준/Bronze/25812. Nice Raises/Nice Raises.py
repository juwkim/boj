g = lambda: [*map(int, input().split())]

n, r = g()
s, t = 0, 0
for _ in range(n):
    num = int(input())
    if num < r:
        s += 1
    elif num > r:
        t += 1

print([0, 1, 2][(s > t) - (s < t)])