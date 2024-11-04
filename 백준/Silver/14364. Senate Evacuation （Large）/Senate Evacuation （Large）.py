import sys
input = sys.stdin.readline
import heapq

for tc in range(1, 1 + int(input())):
    N = int(input())
    P = [(-p, chr(65 + i)) for i, p in enumerate(map(int, input().split()))]
    heapq.heapify(P)
    res = []
    total = sum(-p for p, _ in P)
    while total:
        (a1, b1), (a2, b2) = heapq.heappop(P), heapq.heappop(P)
        MAX = max(-a1-1, -a2)
        if MAX * 2 > total - 1:
            res.append(b1 + b2)
            total -= 2
            if a1 + 1:
                heapq.heappush(P, (a1 + 1, b1))
                heapq.heappush(P, (a2 + 1, b2))
        else:
            res.append(b1)
            total -= 1
            heapq.heappush(P, (a1 + 1, b1))
            heapq.heappush(P, (a2, b2))
    print(f'Case #{tc}:', *res)