N, K = map(int, input().split())
S = input()
ans = K
for ch in set(S):
    cnt = sum(S[i] != ch for i in range(K))
    ans = min(ans, cnt)

    for i in range(K, N):
        if S[i - K] != ch:
            cnt -= 1
        if S[i] != ch:
            cnt += 1
        ans = min(ans, cnt)
print(ans)