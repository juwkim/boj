from collections import Counter

N, M, *A = map(int, open(0).read().split())
A.append(0)
cnt = Counter(A[:M])
a = (9 * M + 9) // 10
k = cnt.most_common(1)[0][0]
ans = "NO"
for i in range(M, N + 1):
    if cnt[k] >= a:
        ans = "YES"
        break
    cnt[A[i]] += 1
    cnt[A[i - M]] -= 1
    k = A[i]
print(ans)