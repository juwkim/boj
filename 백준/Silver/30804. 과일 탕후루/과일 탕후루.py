N, *S = map(int, open(0).read().split())
ans, check, cnt = 0, set(), [0] * 10
l, r = 0, 0
while r < N:
    if len(check) == 2 and S[r] not in check:
        cnt[S[l]] -= 1
        if cnt[S[l]] == 0:
            check.remove(S[l])
        l += 1
    else:
        if cnt[S[r]] == 0:
            check.add(S[r])
        cnt[S[r]] += 1
        r += 1
        ans = max(ans, r - l)
print(ans)