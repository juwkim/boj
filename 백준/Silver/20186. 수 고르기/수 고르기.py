import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
ans = sum(sorted(g(), reverse=True)[:K]) - K * (K - 1) // 2
print(ans)