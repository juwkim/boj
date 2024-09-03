import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

N, M = g()
A = sum(g())
l = []
for i in range(1, N + 1):
    num = sum(g())
    if num <= A:
        l.append((-num, i))
l.sort()
ans = [0] + [l[i][1] for i in range(min(M - 1, len(l)))]
print(*ans)