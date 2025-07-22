K, N = map(int, input().split())
if N == 2 * K - 1:
    print("X-" * (K - 1) + "X")
elif 2 * K <= N <= 3 * K:
    print("-X-" * (N - 2 * K) + "-X" * (3 * K - N))
else:
    print("*")