import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input())):
    l, m = map(int, input().split())
    l *= 100
    left, right = deque(), deque()
    for _ in range(m):
        length, side = input().split()
        length = int(length)
        if side[0] == 'l':
            left.append(length)
        else:
            right.append(length)
    ans = 0
    while left or right:
        length = 0
        if ans & 1:
            while right and length + right[0] <= l:
                length += right.popleft()
        else:
            while left and length + left[0] <= l:
                length += left.popleft()
        ans += 1
    print(ans)