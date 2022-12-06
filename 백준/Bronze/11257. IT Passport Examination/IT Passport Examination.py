g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    n, a, b, c = g()
    p = sum([a, b, c])
    if p >= 55 and a > 10 and b > 7 and c > 11:
        print(n, p, 'PASS')
    else:
        print(n, p, 'FAIL')