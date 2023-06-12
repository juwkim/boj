while (l := [*map(int, input().split())]) != [0, 0, 0]:
    n, m, c = l
    print(((n - 7) * (m - 7) + c) // 2)