import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]
import heapq

N, P0, T = input().split()
N, P0, T = int(N), float(P0), int(T)
hq = []
for idx in range(int(N)):
    S, I, M = input().split()
    hq.append((int(S), int(I), 1 + float(M), idx))
heapq.heapify(hq)
cost, temp = {}, {}
day = 0
while True:
    S, I, M, idx = heapq.heappop(hq)
    if S > day:
        day = S
        for k in temp:
            cost[k] = temp[k]
        temp = {}
        if day >= T:
            break
    if S == 0:
        cost[idx] = P0
    else:
        temp[idx] =  round(sum(cost.values()) * M / len(cost), 2)
    heapq.heappush(hq, (S + I, I, M, idx))
for k in temp:
    cost[k] = temp[k]
for i in range(N):
    print("%.2f" % cost[i])