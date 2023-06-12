while (l := [*map(int, input().split())]) != [0, 0, 0]:
    n, m, c = l
    if c:
        ans = ((n - 7) * (m - 7) + 1) // 2
    else:
        ans = (n - 7) * (m - 7) // 2
    print(ans)