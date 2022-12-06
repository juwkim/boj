g = lambda: [*map(int, input().split())]


p, q = g()
s = input()
if s == 'AABB':
    if q == 7:
        print(8, 9)
    else:
        print(-1)
elif s == 'ABAB':
    if q - p == 2 and q == 8:
        print((p + q) // 2, 9)
    else:
        print(-1)
elif s == 'ABBA':
    if q - p == 3:
        print(p+1, p+2)
    else:
        print(-1)
elif s == 'BAAB':
    if p == 2 and q == 8:
        print(1, 9)
    else:
        print(-1)
elif s == 'BABA':
    if p == 2 and q == 4:
        print(1, 3)
    else:
        print(-1)
else:
    if p == 3:
        print(1, 2)
    else:
        print(-1)