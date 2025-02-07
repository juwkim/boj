import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    N, K, B, T = g()
    X, V = g(), g()
    ans, cnt = 0, 0
    for i in range(N - 1, -1, -1):
        if X[i] + V[i] * T < B:
            cnt += 1
            continue
        ans += cnt
        K -= 1
        if K == 0:
            break
    if K:
        ans = "IMPOSSIBLE"
    print(f"Case #{tc}: {ans}")