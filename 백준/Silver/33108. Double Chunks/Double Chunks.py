from collections import Counter

N, *A = map(int, open(0).read().split())
A = [0] + A
cnt, f = Counter(), False
for i in range(2, N + 1):
    if A[i] != A[i - 2] or f:
        cnt[A[i] + A[i - 1]] += 1
        f = False
    else:
        f = True
print(max(cnt.values()))