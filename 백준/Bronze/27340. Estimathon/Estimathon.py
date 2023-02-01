def g(): return [*map(int, input().split())]

n, m = g()

cnt = 0
for num in g():
    q = num // 4
    if q == 0:
        cnt = -1
        break
    cnt += q

if n < m or cnt < n:
    print('NE')
else:
    print('DA')