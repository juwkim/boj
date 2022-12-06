g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    N, K = g()
    P = max(N - K, 1)
    ans = 2 * (N - P + 1) * (N + P)
    print(ans)