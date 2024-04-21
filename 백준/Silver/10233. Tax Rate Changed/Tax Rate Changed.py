while True:
    x, y, s = map(int, input().split())
    if x == y == s == 0:
        break
    ans = 0
    for a in range(1, s):
        for b in range(1, s - a + 1):
            if a * (100 + x) // 100 + b * (100 + x) // 100 == s:
                ans = max(ans, a * (100 + y) // 100 + b * (100 + y) // 100)
    print(ans)