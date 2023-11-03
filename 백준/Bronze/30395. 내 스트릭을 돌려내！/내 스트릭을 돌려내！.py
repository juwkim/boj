import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
ans, freeze = 0, -2
cnt = 0
for day, num in enumerate(g()):
    if num:
        cnt += 1
    elif day - freeze >= 2:
        freeze = day
    else:
        ans = max(ans, cnt)
        cnt = 0

ans = max(ans, cnt)
print(ans)