g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    R, C = g()
    Map = [[0] * (C + 1), *[[0] + g() for _ in range(R)]]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            a, b, c = Map[i][j - 1], Map[i - 1][j], Map[i - 1][j - 1]
            num = Map[i][j]
            s, idx  = min([(num, 0), (num - a, 1), (num - b, 2), (num - (a + b) // 2, 3), (num - (a + b - c), 4)], key=lambda x: abs(x[0]))
            print(idx, s, end=" ")
        print()