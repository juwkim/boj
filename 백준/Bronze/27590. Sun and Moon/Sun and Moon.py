d1, y1 = map(int, input().split())
d2, y2 = map(int, input().split())

cur = y1 - d1 + d2
while cur % y2:
    cur += y1
print(cur - d2)