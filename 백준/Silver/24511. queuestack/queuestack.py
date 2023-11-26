import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

N = int(input())
queuestack = deque(num for is_stack, num in zip(g(), g()) if not is_stack)
M = int(input())
ans = []
for num in g():
    queuestack.appendleft(num)
    ans.append(queuestack.pop())
print(*ans)