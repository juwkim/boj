g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    N, M = g()
    print(f'Case {_}: {M - N + 1}')