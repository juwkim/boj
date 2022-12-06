a, b, c = map(int, input().split())
s = abs(a) + abs(b)
if c >= s and (c - s) % 2 == 0:
    print('YES')
else:
    print('NO')