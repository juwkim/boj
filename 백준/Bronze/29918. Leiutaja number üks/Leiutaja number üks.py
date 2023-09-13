import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N0, M0 = g()
Max = 0
for _ in range(5):
    N, M = g()
    Max = max(Max, N + 10 * M)
ans = max(0, Max + 1 - (N0 + 10 * M0))
print(ans)