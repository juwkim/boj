g = lambda: [*map(float, input().split())]

ex_rate = [g() for _ in range(5)]
while (s:= input()) != '0':
    N, *C, m = s.split()
    C = [*map(int, C)]
    m = float(m)
    for i, j in zip([1] + C, C):
        m *= ex_rate[i-1][j-1]
        m = round(m, 2)
    m *= ex_rate[C[-1]-1][0]
    print('%.2f' % m)