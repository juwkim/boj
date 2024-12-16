N, K, M = map(int, input().split())
q, r = divmod(M, 2 * (N - 1) * K)
ans = [2 * q * K] * N
ans[0], ans[-1] = q * K, q * K
for i in range(N - 1):
    if r > K:
        ans[i] += K
        r -= K
    else:
        ans[i] += r
        r = 0
        break
for i in range(N - 1, 0, -1):
    if r > K:
        ans[i] += K
        r -= K
    else:
        ans[i] += r
        r = 0
        break
print(*ans)