N, K = map(int, input().split())
S = input()
ans = K
for ch in set(S):
    cnt = sum(S[i] != ch for i in range(K))
    ans = min(ans, cnt)
    for i in range(K, N):
        cnt += (S[i] != ch) - (S[i - K] != ch)
        ans = min(ans, cnt)
print(ans)