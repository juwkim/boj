import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

N, M = map(int, input().split())
P = {chr(65 + i): int(input()) for i in range(26)}
cnt = Counter()
for _ in range(N):
    cnt[input()] += 1
ans = -1
for _ in range(M):
    word = Counter(input())
    if all(cnt[k] >= word[k] for k in word):
        ans = max(ans, sum(P[k] * word[k] for k in word))
print(ans)