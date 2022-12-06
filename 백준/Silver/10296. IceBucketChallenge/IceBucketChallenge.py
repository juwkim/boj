g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    G, K = g()
    cur = 1
    ans = 0
    while True:
        if G - 100 * cur <= 0:
            break
        else:
            ans += 1
            G -= 10
            cur += K - 1
    print(ans)