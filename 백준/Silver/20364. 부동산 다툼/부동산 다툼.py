import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
visited = set()
for _ in range(Q):
    x = int(input())
    ans, cur = 0, x
    while cur != 1:
        if cur in visited:
            ans = cur
        cur >>= 1
    if ans == 0:
        visited.add(x)
    print(ans)