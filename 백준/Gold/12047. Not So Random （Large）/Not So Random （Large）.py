for t in range(int(input())):
    N, X, K, A, B, C = map(int, input().split())
    AB, BC = (A + B) / 100, (B + C) / 100
    a, b, c = 1, 0, 1
    for _ in range(N):
        a *= BC
        b = b * AB + (1 - b) * BC
        c = c * AB + (1 - c) * BC
    ans = sum(((0, a), (b, c))[K >> i & 1][X >> i & 1] * (1 << i) for i in range(max(X, K).bit_length()))
    print(f"Case #{t+1}: {ans:.10f}")