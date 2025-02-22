for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans = [['.'] * (2 * (a + b) + 1) for _ in range(2 * (b + c) + 1)]
    s, t = "+-" * a + "+", "/." * a + "/"
    for i in range(0, 2 * b, 2):
        ans[i][2 * b - i:2 * a + 2 * b + 1 - i] = s
        ans[i + 1][2 * b - i - 1:2 * a + 2 * b - i] = t
    for j in range(2 * (a + b), 2 * a, -2):
        for i in range(2 * (a + b) - j + 1, 2 * (a + b + c) - j + 1):
            ans[i][j] = "+|"[i & 1]
        for i in range(2 * (a + b) - j + 2, 2 * (a + b + c) - j + 2):
            ans[i][j - 1] = "./"[i & 1]
    for i in range(2 * b, 2 * (b + c) + 1):
        for j in range(2 * a + 1):
            ans[i][j] = ("+-", "|.")[i & 1][j & 1]
    for l in ans:
        print(*l, sep='')