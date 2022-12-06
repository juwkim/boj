h, m, dh, dm, c = map(int, input().split())
a, b = divmod(((h + dh) * 60 + m + dm) % 720, 60)
if c == 1:
    print(a, b)
elif b % 12:
    c = 5 * a + b / 12
    print(int(c), (int(c) + 1) % 60)
else:
    print('@', 5 * a + b // 12)