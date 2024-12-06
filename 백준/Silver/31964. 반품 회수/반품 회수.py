import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
X = g()
T = g()
ans = max(X[-1], T[-1])
for i in range(N - 2, -1, -1):
    ans = max(ans + X[i + 1] - X[i], T[i])
ans += X[0]
print(ans)