import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
ans = sum(g()) + sum(i * d for i, d in enumerate(sorted(g(), reverse=True)))
print(ans)