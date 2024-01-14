import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]


buf = []
N = int(input())
for _ in range(N):
    day, cow, milk = input().split()
    buf.append((int(day), cow, int(milk)))
buf.sort()
cnt = [7, 7, 7]
cur = [0, 1, 2]
ans = 0
for day, cow, milk in buf:
    if cow == "Bessie":
        idx = 0
    elif cow == "Elsie":
        idx = 1
    else:
        idx = 2
    cnt[idx] += milk
    nxt = [i for i in range(3) if cnt[i] == max(cnt)]
    if nxt != cur:
        ans += 1
        cur = nxt
print(ans)