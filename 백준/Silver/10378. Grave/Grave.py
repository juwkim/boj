g = lambda: [*map(int, input().split())]

x1, y1, x2, y2 = g()
x3, y3, x4, y4 = g()
w, h = g()
ans = 'No'
if w <= max(x3 - x1, x2 - x4):
    if h <= y2 - y1:
        ans = 'Yes'
elif w <= x2 - x1 and h <= max(y3 - y1, y2 - y4):
    ans = 'Yes'
print(ans)