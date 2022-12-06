x, y, z = map(int, input().split())
a, b, c, d, e, f = [int(input()) for _ in range(6)]
l = [e - x + (d + f) / 2, a - y + (b + f) / 2, c - z + (b + d) / 2]
for i in l:
    i = max(0, i)
    if i % 1:
        print("%.1f" % i, end =' ')
    else:
        print(int(i), end =' ')