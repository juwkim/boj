g = lambda: [*map(int, input().split())]
f = lambda: [*map(float, input().split())]

for k in range(1, 1 + int(input())):
    B, D = g()
    basic = f()
    for _ in range(D + 1):
        basic.append(sum(i*j for i, j in zip(basic, f())))
    print(f'Data Set {k}:\n{basic[-1]:.2f}\n')