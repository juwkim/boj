K, N = map(int, input().split())
if N == 2 * K - 1:
    print("X-" * (K - 1) + "X")
elif 2 * K <= N <= 3 * K:
    for _ in range(N - 2 * K):
        print("-X-", end="")
    for _ in range(3 * K - N):
        print("-X", end="")
else:
    print("*")