import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

s = [*input()]
k = int(input())
buf = [[] for _ in range(k)]
for i, c in enumerate(s):
    buf[i % k].append(c)
for i in range(k):
    buf[i].sort()
ans = []
for i in range(len(s)):
    ans.append(buf[i%k][i//k])
print(*ans, sep='')