import sys
input = sys.stdin.readline
import math

while N := int(input()):
    arrows = [0] * (N + 1)
    for _ in range(N):
        a, b = map(int, input().split())
        arrows[a] = b
    visited = [False] * (N + 1)
    result = []
    for i in range(1, N + 1):
        if not visited[i]:
            cnt, cur = 0, i
            while not visited[cur]:
                visited[cur] = True
                cur = arrows[cur]
                cnt += 1
            result.append(cnt)
    print(math.lcm(*result))