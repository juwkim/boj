import datetime

x, n = map(int, input().split())
d, m, g = map(int, input().split())
c = 2 * n * x - n - 1
a = datetime.datetime(g, m, d) + datetime.timedelta(c)
print(*a.timetuple()[:3][::-1])