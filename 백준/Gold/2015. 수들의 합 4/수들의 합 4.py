from collections import Counter

N, K, *A = map(int, open(0).read().split())
px = [0] * (N + 1)
for i in range(N):
    px[i + 1] = px[i] + A[i]
ans, cnt = 0, Counter()
for i in range(N):
    cnt[px[i]] += 1
    ans += cnt[px[i + 1] - K]
print(ans)