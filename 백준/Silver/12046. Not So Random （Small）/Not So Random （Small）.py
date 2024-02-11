import sys
input = sys.stdin.readline
ith_bit = lambda x, i: (x >> i) & 1
for tc in range(1, 1 + int(input())):
    N, X, K, A, B, C = map(int, input().split())
    ans = 0
    for i in range(max(X, K).bit_length()):
        a, b = ((0, 1), (1, 0))[ith_bit(X, i)]
        if ith_bit(K, i):
            for _ in range(N):
                a = a * (A + B) / 100 + b * (B + C) / 100
                b = 1 - a
        else:
            for _ in range(N):
                a = a * (B + C) / 100
                b = 1 - a
        ans += a * (1 << i)
    print(f"Case #{tc}: {ans}")