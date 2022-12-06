A, B, K = map(int, input().split())
if A >= 2*K and B >= 2*K:
    print(2*max(A // K + (B - 2 * K) // K, B // K + (A - 2 * K) // K))
elif A >= 2*K and B >= K:
    print(A // K)
elif B >= 2*K and A >= K:
    print(B // K)
else:
    print(int(A >= K and B >= K))