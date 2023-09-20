import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

ans = 0
l, h = float('inf'), float('inf')
for _ in range(int(input())):
    num = int(input())
    if num > h:
        h = num
    else:
        ans = max(ans, h - l)
        l, h = num, num
ans = max(ans, h - l)
print(ans)