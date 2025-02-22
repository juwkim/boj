import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    M, R, N = g()
    X = g()
    ans, cover = 0, 0
    for i in range(N - 1):
        if X[i] - cover > R:
            ans = "IMPOSSIBLE"
            break
        if X[i + 1] - cover > R:
            cover = X[i] + R
            ans += 1
    else:
        if cover < M:
            cover = X[-1] + R
            ans += 1
        if cover < M:
            ans = "IMPOSSIBLE"
    print(f"Case #{tc}: {ans}")