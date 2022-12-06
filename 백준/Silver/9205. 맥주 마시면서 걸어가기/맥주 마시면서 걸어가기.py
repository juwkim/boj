g = lambda: [*map(int, input().split())]

from collections import deque
def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
for _ in range(int(input())):
    n = int(input())
    x, y = g()
    stores = [g() for _ in range(n+1)]
    dest = stores[-1]
    
    dq = deque([(x, y)])
    visited = bytearray(n+1)
    ans = 'sad'
    while dq:
        pos = dq.popleft()
        if pos == dest:
            ans = 'happy'
            break
        for i in range(n+1):
            if visited[i] == 0:
                if dist(pos, stores[i]) <= 1000:
                    visited[i] = 1
                    dq.append(stores[i])
    print(ans)