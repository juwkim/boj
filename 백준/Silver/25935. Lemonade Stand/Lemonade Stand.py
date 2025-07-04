import sys
input = sys.stdin.readline
g = lambda: map(int, input().split())

for _ in range(int(input())):
    d, x, s = g()
    ans = 0
    lemon_price, sugar_price = 50, 500
    sugar_left = 0
    for _ in range(d):
        c, pl, ps = g()
        lemon_price = min(lemon_price, pl)
        sugar_price = min(sugar_price, ps)
        ans += c * x * lemon_price
        sugar_need = c * s
        if sugar_left >= sugar_need:
            sugar_left -= sugar_need
        else:
            bags = (sugar_need - sugar_left + 79) // 80
            sugar_left += 80 * bags - sugar_need
            ans += bags * sugar_price
    print(ans)