import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    S = input()
    for i in range(len(S)):
        cnt[S[i:]] += 1
print(sum(v&1 for v in cnt.values()))