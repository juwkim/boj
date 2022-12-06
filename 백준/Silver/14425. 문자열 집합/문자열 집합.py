import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
s = {input() for _ in range(N)}
cnt = 0
for _ in range(M):
    cnt += input() in s
print(cnt)