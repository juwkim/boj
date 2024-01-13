import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

T = Counter(input())
N = int(input())
cost, book = [], []
for _ in range(N):
    a, b = input().split()
    cost.append(int(a))
    book.append(Counter(b))

ans = 1e9
used = bytearray(N)
def dfs(i, cnt):
    global ans
    if cnt >= T:
        ans = min(ans, sum(cost[j] for j in range(N) if used[j]))
        return
    if i == N:
        return
    dfs(i + 1, cnt)
    used[i] = 1
    dfs(i + 1, cnt + book[i])
    used[i] = 0

dfs(0, Counter())
if ans == 1e9:
    ans = -1
print(ans)