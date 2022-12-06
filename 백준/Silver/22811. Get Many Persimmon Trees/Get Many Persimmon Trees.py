g = lambda: [*map(int, input().split())]

while N := int(input()):
    W, H = g()
    trees = [g() for _ in range(N)]
    S, T = g()
    ans = 0
    for i in range(1, W-S+2):
        for j in range(1, H-T+2):
            num = 0
            for x, y in trees:
                if i <= x < i + S and j <= y < j + T:
                    num += 1
            ans = max(ans, num)
    print(ans)
