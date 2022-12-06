g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n, v = g()
    ans = 0
    ads = [g() for _ in range(n)]
    for _ in range(v):
        ad1, ad2, click = g()
        if ads[ad1-1][0] == 1 or click == 1:
            ans += ads[ad1-1][1]
        if ads[ad2-1][0] == 1 or click == 2:
            ans += ads[ad2-1][1]
    print(f'Data Set {cnt}:\n{ans}\n')