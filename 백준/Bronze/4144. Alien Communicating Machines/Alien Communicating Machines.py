g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    x, y, z = input().split()
    x, y = map(int, [x, y])
    t = int(z, x)
    ans = ''
    while True:
        t, q = divmod(t, y)
        ans = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[q] + ans
        if t == 0:
            break
    print(ans)