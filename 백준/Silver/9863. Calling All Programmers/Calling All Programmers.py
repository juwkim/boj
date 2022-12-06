from collections import deque
while (s:=input()) != '0 0 0':
    n, m, k = map(int, s.split())
    dq = deque(range(1, n+1))
    for _ in range(k):
        dq.rotate(1-m)
        ans = dq.popleft()
    print(ans)