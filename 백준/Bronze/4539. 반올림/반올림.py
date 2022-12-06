g = lambda: [*map(int, input().split())]
f = lambda: int(input())
for _ in range(f()):
    comp = 10
    num = f()
    i = 1
    while num > comp:
        num = round(num+.1, -i)
        i += 1
        comp *= 10
    print(int(num))