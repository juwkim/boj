import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

N, D = g()
dp = [*range(D + 1)]
dic = defaultdict(lambda: defaultdict(lambda: float('inf')))
for _ in range(N):
    s, e, d = g()
    dic[e][s] = min(dic[e][s], d)
for i in range(2, D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    for s in dic[i]:
        d = dic[i][s]
        dp[i] = min(dp[i], dp[s] + d)
print(dp[D])