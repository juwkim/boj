import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, M, Q = g()
    V = g()
    P, H = zip(*[g() for _ in range(N)])
    ans = 1e9
    def solve(i, q, cost):
        global ans
        if i == N:
            ans = min(ans, cost)
            return
        if P[i] == 0:
            solve(i + 1, q, max(cost, 0))
        else:
            for h in range(max(0, H[i] - (Q - q)), min(H[i] + (Q - q) + 1, M)):
                if P[i] * V[h] < 0:
                    p, v = abs(P[i]), abs(V[h])                    
                    solve(i + 1, q + abs(h - H[i]), max(cost, (p + v - 1) // v))
    solve(0, 0, -1)
    if ans == 1e9:
        ans = "IMPOSSIBLE"
    print(f"Case #{tc}: {ans}")