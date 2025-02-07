import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

N, K = g()
ans, cur = 0, 0
Xprev, Yprev = 0, 0
for _ in range(int(input())):
    X, Y = g()
    def solve():
        global ans, cur, Xprev, Yprev
        if X == Xprev:
            Yprev += Y
        else:
            if cur + Yprev >= K:
                ans += 1
                if cur + Yprev == K:
                    cur = 0
                else:
                    cur = Yprev
            else:
                cur += Yprev
            cur += X - Xprev - 1
            q, cur = divmod(cur, K)
            ans += q
            Xprev, Yprev = X, Y + 1
    solve()
X, Y = N + 1, 0
solve()
if cur:
    ans += 1
print(ans)