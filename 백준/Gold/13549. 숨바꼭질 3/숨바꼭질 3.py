g = lambda: [*map(int, input().split())]

import heapq
N, K = g()
if K > N:
    visited = bytearray(100001)
    visited[N] = 1
    hq = [(0, N)]
    heapq.heapify(hq)
    
    while hq:
        d, num = heapq.heappop(hq)
        if num == K:
            print(d)
            break

        pos = num * 2
        if 0 <= pos < 100001:
            if visited[pos] == 0:
                visited[pos] = 1
                heapq.heappush(hq, (d, pos))
        
        for pos in (num + 1, num - 1):
            if 0 <= pos < 100001:
                if visited[pos] == 0:
                    visited[pos] = 1
                    heapq.heappush(hq, (d+1, pos))
else:
    print(N - K)