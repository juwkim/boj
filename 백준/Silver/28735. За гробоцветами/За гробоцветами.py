import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

ans = 'No'
n = int(input())
x1, y1 = g()
x2, y2 = g()
idx = -1
for i in range(3, n + 1):
    x, y = g()
    if (x - x1) * (y2 - y1) != (y - y1) * (x2 - x1):
        ans = 'Yes'
        idx = i
        break
print(ans)
if ans == 'Yes':
    print(1, 2, idx)