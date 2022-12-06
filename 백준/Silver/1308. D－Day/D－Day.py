import datetime as d
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
if y2 - y1 > 1000 or (y2 - y1 == 1000 and m2 > m1) or (y2 - y1 == 1000 and m2 == m1 and d2 >= d1):
    print('gg')
else:
    a = d.datetime(y1, m1, d1)
    b = d.datetime(y2, m2, d2)
    print("D-%d" % (b - a).days)