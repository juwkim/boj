n = int(input())
if n == 2:
    print(-1)
else:
    m = n + 1 >> 1
    a = [['.'] * m for _ in range(m)]
    for i in range(m): a[i][0] = 'o'
    a[-1] = 'o' * m
    if n & 1 == 0:
        a[-2][1] = 'o'
    print(m)
    for l in a:
        print(*l, sep='')