import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

S, P = g()
DNA = input()
ACGT = {k: v for k, v in zip("ACGT", g())}
cnt = Counter(DNA[:P])
ans = +all(cnt[k] >= ACGT[k] for k in "ACGT")
for i in range(P, S):
    cnt[DNA[i]] += 1
    cnt[DNA[i - P]] -= 1
    ans += all(cnt[k] >= ACGT[k] for k in "ACGT")
print(ans)