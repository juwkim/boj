import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
paper = set(g())
empty = [i for i in range(1, N+1) if i not in paper]
ans = 0
s = -1
for i in range(len(empty)):
    if s == -1:
        s = empty[i]
    elif empty[i] - empty[i-1] >= 4:
        ans += 5 + 2 * (empty[i-1] - s + 1)
        s = empty[i]
if s != -1:
    ans += 5 + 2 * (empty[-1] - s + 1)
print(ans)