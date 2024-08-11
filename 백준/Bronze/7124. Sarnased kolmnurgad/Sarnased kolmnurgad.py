import sys
g = lambda: map(int, sys.stdin.readline().split())
d = lambda p1, p2: (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

x1, y1, x2, y2, x3, y3 = g()
s1, t1, s2, t2, s3, t3 = g()
a = [d((x1, y1), (x2, y2)), d((x2, y2), (x3, y3)), d((x3, y3), (x1, y1))]
b = [d((s1, t1), (s2, t2)), d((s2, t2), (s3, t3)), d((s3, t3), (s1, t1))]
ans = -1
for l in ((0, 1, 2), (1, 2, 0), (2, 0, 1), (0, 2, 1), (1, 0, 2), (2, 1, 0)):
    if a[0] / b[l[0]] == a[1] / b[l[1]] == a[2] / b[l[2]]:
        ans = (a[0] / b[l[0]])**.5
        break
print(ans)