import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M, D = g()
ans = 'YES'
for l in zip(*[sorted(g()) for _ in range(N)]):
    if any(a >= b + D for a, b in zip(l, l[1:])):
        ans = 'NO'
        break
print(ans)