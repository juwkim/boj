import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

def solve(X, Y):
    global ans, cur, Xprev, Yprev
    if X == Xprev:
        Yprev += Y
    else:
        if cur + Yprev > K:
            ans += 1
            cur = Yprev
        elif cur + Yprev == K:
            ans += 1
            cur = 0
        else:
            cur += Yprev
        ans += (cur + X - Xprev - 1) // K
        cur = (cur + X - Xprev - 1) % K
        Xprev, Yprev = X, Y + 1
N, K = g()
ans, cur = 0, 0
Xprev, Yprev = 0, 0
for _ in range(int(input())):
    solve(*g())
solve(N + 1, 0)
if cur: ans += 1
print(ans)