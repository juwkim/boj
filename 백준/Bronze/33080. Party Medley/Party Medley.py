from itertools import combinations

cnt, Max = 0, 0
N, M, *A = map(int, open(0).read().split())
for l in combinations(A, 3):
    if max(l) - min(l) <= M:
        cnt += 1
        Max = max(Max, sum(l))
if cnt:
    print(cnt, Max)
else:
    print(-1)