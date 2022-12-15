g = lambda: map(int, input().split())
Max = 1000000
for step in range(1, 1 + int(input())):
    a, b, c, d = map(min, zip(g(), g(), g()))
    if a + b + c + d < Max:
        ans = 'IMPOSSIBLE'
    elif a + b + c < Max:
        ans = a, b, c, Max - (a + b + c)
    elif a + b < Max:
        ans = a, b, Max - (a + b), 0
    elif a < Max:
        ans = a, Max - a, 0, 0
    else:
        ans = Max, 0, 0, 0
    if ans == 'IMPOSSIBLE':
        print(f'Case #{step}: IMPOSSIBLE')
    else:
        print(f'Case #{step}:', *ans)