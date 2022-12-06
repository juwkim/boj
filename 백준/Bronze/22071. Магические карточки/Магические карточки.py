g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    n, l = g()
    grisha = sum(sorted(g())[:l])
    dima = sum(sorted(g())[-l:])
    print('YES' if grisha > dima else 'NO')