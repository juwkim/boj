for t in range(int(input())):
    N, X, K, A, B, C = map(int, input().split())
    a, b, c = 1, 0, 1
    for _ in range(N):
        a *= (B + C) / 100
        b = (b * A + B + (1 - b) * C) / 100
        c = (c * A + B + (1 - c) * C) / 100
    ans = sum(((0, a), (b, c))[K >> i & 1][X >> i & 1] * (1 << i) for i in range(max(X, K).bit_length()))
    print(f"Case #{t+1}: {ans:.10f}")