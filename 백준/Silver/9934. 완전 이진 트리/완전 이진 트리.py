import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque

K = int(input())
nums = g()
dq = deque([len(nums) // 2])
dist = 2 ** (K - 2)
for _ in range(K):
    for _ in range(len(dq)):
        idx = dq.popleft()
        print(nums[idx], end=" ")
        dq.append(idx - dist)
        dq.append(idx + dist)
    dist //= 2
    print()