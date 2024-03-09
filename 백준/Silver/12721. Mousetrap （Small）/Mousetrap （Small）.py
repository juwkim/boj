import sys
input = sys.stdin.readline
from collections import deque

for tc in range(1, 1 + int(input())):
    K = int(input())
    n, *d = map(int, input().split())
    a = [0] * (K + 1)
    dq = deque(range(1, K + 1))
    for i in range(K):
        dq.rotate(-i)
        a[dq.popleft()] = i + 1
    ans = [a[i] for i in d]
    print(f"Case #{tc}:", *ans)