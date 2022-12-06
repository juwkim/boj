S, K = map(int, input().split())
r, q = divmod(S, K)
ans = r ** (K - q) * (r + 1) ** q
print(ans)