g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    m, n = g()
    A = set(g())
    B = set(g())
    print(+(2 * len(A & B) > len(A | B)))