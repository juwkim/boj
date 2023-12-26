import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from queue import PriorityQueue
qu = PriorityQueue()
for _ in range(int(input())):
    a, *nums = g()
    if a == 0:
        if qu.empty():
            print(-1)
        else:
            print(-qu.get())
    else:
        for num in nums:
            qu.put(-num)