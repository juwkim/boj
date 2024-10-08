import sys
input = sys.stdin.readline

ans = 1e9
for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 * x2 < 0:
        num = (x1 * y2 - x2 * y1) / (x1 - x2)
        if num > 0:
            ans = min(ans, num)
if ans == 1e9:
    print(-1.0)
else:
    print(ans)