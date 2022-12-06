x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
print(max(max(x4, x2) - min(x3, x1), max(y4, y2) - min(y3, y1))**2)