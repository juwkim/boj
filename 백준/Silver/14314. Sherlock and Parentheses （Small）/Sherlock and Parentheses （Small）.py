g = lambda: [*map(int, input().split())]


for _ in range(1, 1 + int(input())):
    num = min(g())
    print(f'Case #{_}:', num * (num + 1) // 2)