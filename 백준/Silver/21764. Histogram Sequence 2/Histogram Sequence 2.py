import sys
input = lambda: sys.stdin.readline().rstrip()
from math import inf

MOD = 10 ** 9 + 7
N = int(input())
h = [inf, *map(int, input().split()), inf]
ans = 1
for i in range(1, N + 1):
    ans = ans * min(h[i - 1], h[i], h[i + 1]) % MOD
print(ans)