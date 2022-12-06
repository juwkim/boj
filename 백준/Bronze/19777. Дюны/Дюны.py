g = lambda: [*map(int, input().split())]

n, m = g()
tonado = [g() for _ in range(n)]
for _ in range(m):
    num = int(input())
    ans = 0
    for l, r, x in tonado:
        if l <= num <= r:
            if (num - l) & 1:
                ans -= x
            else:
                ans += x
    print(ans)