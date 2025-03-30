N, D, K, *s = map(int, open(0).read().split())
ans = 0
cnt = [0] * N
for _ in range(D):
    if any(a + b > K for a, b in zip(cnt, s)):
        ans += 1
        cnt = [0] * N
    for i in range(N): cnt[i] += s[i]
print(ans)