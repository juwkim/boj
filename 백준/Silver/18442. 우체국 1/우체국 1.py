from itertools import combinations

V, P, L, *A = map(int, open(0).read().split())
ans, dist = None, 1e14
for l in combinations(A, P):
    cur = sum(min(min(abs(num - t), L - abs(num - t)) for t in l) for num in A)
    if cur < dist:
        ans, dist = l, cur
print(dist)
print(*ans)