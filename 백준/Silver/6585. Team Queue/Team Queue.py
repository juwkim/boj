import sys
input = sys.stdin.readline
from collections import deque

tc = 1
while t:=int(input()):
    d = {}
    for i in range(t):
        n, *nums = map(int, input().split())
        for num in nums:
            d[num] = i
    dq = deque()
    l = [deque() for _ in range(t)]
    print(f"Scenario #{tc}")
    while (s := input())[0] != 'S':
        if s[0] == 'D':
            idx = dq[0]
            print(l[idx].popleft())
            if not l[idx]:
                dq.popleft()
        else:
            n = int(s.split()[1])
            if not l[d[n]]:
                dq.append(d[n])
            l[d[n]].append(n)
    tc += 1
    print()