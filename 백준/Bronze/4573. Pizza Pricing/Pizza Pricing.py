g = lambda: [*map(int, input().split())]

cnt = 1
while n:=int(input()):
    ans = max([g() for _ in range(n)], key=lambda x: x[0] * x[0] / x[1])[0]
    print(f'Menu {cnt}: {ans}')
    cnt += 1