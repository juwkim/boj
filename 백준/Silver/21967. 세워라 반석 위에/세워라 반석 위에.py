import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

N = int(input())
ans = 0
check = [0] * 11
dq = deque()
for i, num in enumerate(g()):
    dq.append(num)
    check[num] += 1
    while max(i for i in range(1, 11) if check[i]) - min(i for i in range(1, 11) if check[i]) > 2:
        check[dq.popleft()] -= 1
    ans = max(ans, len(dq))
print(ans)