import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n, k = g()
a = g()
t = input().split()
px = [0]
for i in range(1, max(a) + 1):
    px.append(px[-1] + any(c in str(i) for c in t))
print(sum(px[l] for l in a))