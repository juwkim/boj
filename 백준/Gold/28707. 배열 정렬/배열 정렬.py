import sys; input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())

# 주어지는 배열을 하나의 노드로 이용하기 위해 문자열로 만들어준다.
A = ''
for c in input().split():
    A += str(int(c) - 1)

M = int(input())
Q = [tuple(map(int, input().split())) for _ in range(M)]

pq = [(0, A)]
dist = dict() # 문자열이 키인 맵을 dist 배열로 사용한다.
dist[A] = 0

# 다익스트라
while pq:
    cost, now = heappop(pq)
    if dist[now] < cost:
        continue
    for l, r, c in Q:
        nxt = now[:l - 1] + now[r - 1] + now[l:r - 1] + now[l - 1] + now[r:] # 조작 결과
        if nxt not in dist or dist[nxt] > cost + c: # 조작 결과인 키가 dist에 있는지부터 확인한다.
            dist[nxt] = cost + c
            heappush(pq, (cost + c, nxt))

# 주어진 배열을 정렬한 다음, 결과가 저장되어 있는지 확인한다.
A = ''.join(sorted(A))
if A not in dist:
    print(-1)
else:
    print(dist[A])