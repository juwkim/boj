import sys
input = lambda: sys.stdin.readline().rstrip('\n')

from collections import deque
g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    N = int(input())
    dq = deque()
    ans = []
    for num in g():
        if len(dq) and num == dq[0]:
            dq.popleft()
        else:
            ans.append(num)
            dq.append(num * 4 // 3)
            
    print(f'Case #{cnt}:', *ans)