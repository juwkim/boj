g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    a = sorted(g())
    b = sorted(g())
    ans = 'NO'
    if a == b and a[0] ** 2 + a[1] ** 2 == a[2] ** 2:
        ans = 'YES'
    print(ans)