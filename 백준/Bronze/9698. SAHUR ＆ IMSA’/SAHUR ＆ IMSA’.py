g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    h, m = g()
    t = (h * 60 + m - 45) % 1440
    print(f'Case #{_}:', t//60, t%60)