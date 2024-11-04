import sys
import heapq
input = sys.stdin.readline

for tc in range(1, 1 + int(input())):
    input()
    total = sum(nums:=[*map(int, input().split())])
    P = [(-p, chr(65 + i)) for i, p in enumerate(nums)]
    heapq.heapify(P)
    ans = []
    while total:
        (a1, b1), (a2, b2) = heapq.heappop(P), heapq.heappop(P)
        if max(-a1-1, -a2) * 2 >= total:
            ans.append(b1 + b2)
            total -= 2
            if a1 + 1:
                heapq.heappush(P, (a1 + 1, b1))
                heapq.heappush(P, (a2 + 1, b2))
        else:
            ans.append(b1)
            total -= 1
            heapq.heappush(P, (a1 + 1, b1))
            heapq.heappush(P, (a2, b2))
    print(f'Case #{tc}:', *ans)