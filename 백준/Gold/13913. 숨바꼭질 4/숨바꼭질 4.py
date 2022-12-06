g = lambda: [*map(int, input().split())]

from collections import deque
N, K = g()
if K > N:
    visited = bytearray(100001)
    visited[N] = 1
    dq = deque([(N, 0)])
    dic = {N: [N]}
    while dq:
        num, d = dq.popleft()
        if num == K:
            print(d)
            print(*dic[num])
            break
        
        for pos in (num + 1, num - 1, num * 2):
            if 0 <= pos < 100001:
                if visited[pos] == 0:
                    visited[pos] = 1
                    dq.append((pos, d + 1))
                    dic[pos] = dic[num] + [pos]
        del dic[num]
else:
    print(N - K)
    print(*range(N, K - 1, -1))