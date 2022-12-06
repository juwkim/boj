count = 0
n = int(input())
for _ in range(n):
    x1, y1, x2, y2 = map(float, input().split())
    x1, x2 = map(lambda x: x -(x<0), [x1, x2])
    count += (x1%1 == 0 or x2%1 == 0 or abs(int(x1) - int(x2)))
print(2*n/count)