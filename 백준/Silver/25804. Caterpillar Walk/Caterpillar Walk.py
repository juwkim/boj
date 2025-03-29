import sys
input = sys.stdin.readline

n = int(input())
ans, prvx, prvh = 100, 0, 0
for s, w, h in sorted([*map(int, input().split())] for _ in range(n)):
    if s == prvx:
        ans += abs(h - prvh)
    else:
        ans += prvh + h
    prvx = s + w
    prvh = h
ans += prvh
print(ans)