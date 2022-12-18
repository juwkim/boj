r = (1 + 5 ** .5) / 2
for _ in range(int(input())):
    a, b = map(float, input().split())
    if abs(a / b - r) < 0.01 * r:
        print('golden')
    else:
        print('not')