import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
d, r = zip(*[g() for _ in range(n)])
r = sorted(r)
dmin = min(min(d), r[n//2])
ans = sum(abs(dmin - r[i]) for i in range(n))
print(ans)