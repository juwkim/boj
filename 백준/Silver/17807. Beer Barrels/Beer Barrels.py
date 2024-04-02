A, B, K, C = map(int, input().split())
if C not in (A, B):
    print(0)
elif A == B:
    print(K)
else:
    mod = 10**9 + 7
    print(K * pow(2, K - 1, mod) % mod)