import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N = int(input())
X, S = g()
ans = "NO"
for _ in range(N):
    c, p = g()
    if c <= X and p > S:
        ans = "YES"
        break
print(ans)