import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
import heapq

input()
d = [i + a for i, a in enumerate(g())]
Q = int(input())
hq = [(a, i) for i, a in enumerate(g())]
heapq.heapify(hq)
ans, idx = [0] * Q, 0
while hq:
    a, i = heapq.heappop(hq)
    while d[idx] < a:
        idx += 1
    ans[i] = idx + 1
print(*ans)