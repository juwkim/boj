for tc in range(1, 1 + int(input())):
    N, X, K, A, B, C = map(int, input().split())
    AB, BC = (A + B) / 100, (B + C) / 100    
    ans = 0
    for i in range(max(X, K).bit_length()):
        a = X >> i & 1
        if K >> i & 1:
            for _ in range(N):
                a = a * AB + (1 - a) * BC
        else:
            for _ in range(N):
                a *= BC
        ans += a * (1 << i)
    print(f"Case #{tc}: {ans:.10f}")