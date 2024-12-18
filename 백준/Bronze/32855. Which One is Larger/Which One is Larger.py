a, b = input(), input()
a1, b1 = float(a), float(b)
a2, b2 = [*map(int, a.split('.'))], [*map(int, b.split('.'))]
if a1 > b1 and a2 > b2:
    print(a)
elif a1 < b1 and a2 < b2:
    print(b)
else:
    print(-1)