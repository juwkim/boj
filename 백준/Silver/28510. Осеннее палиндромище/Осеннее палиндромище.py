from collections import Counter, deque

def solve():
    global s
    cnt, dq = Counter(s), deque()
    for k, v in cnt.items():
        if v & 1:
            if dq:
                return False
            dq.append(k)
    for k, v in cnt.items():
        for _ in range(v >> 1):
            dq.append(k)
            dq.appendleft(k)
    s = dq
    return True

n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = "NO"
if solve():
    s = [*map("".join, zip(*s))]
    if solve():
        ans = "YES"
print(ans)