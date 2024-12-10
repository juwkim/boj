import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from collections import Counter

N = int(input())
cnt = Counter(g())
for _ in range(int(input())):
    A, B = Counter(g()[1:]), Counter(g()[1:])
    if all(cnt[k] >= A[k] for k in A):
        for k in A:
            cnt[k] -= A[k]
        for k in B:
            cnt[k] += B[k]
print(sum(cnt.values()))
for k in cnt:
    print(*[k] * cnt[k], end=' ')