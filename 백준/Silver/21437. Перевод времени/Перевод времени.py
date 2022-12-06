g = lambda: [*map(int, input().split())]

m = int(input())
d1, d2 = g()
k = int(input())

time_type = d1
if m >= 150 - 30 * time_type:
    m += time_type * 60
    time_type = 0

for i in range(k):
    r, q = divmod(m, 60)
    r %= 24
    print('%02d:%02d' % (r, q))
    m += 1
    if m == 150 - 30 * time_type:
        m += time_type * 60
        time_type = 0
    elif m == 1440:
        time_type = d2
        m -= 1440