for tc in range(1, int(input()) + 1):
    alive = [[0] * 101 for _ in range(101)]
    cnt = 0
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                alive[x][y] = 1
                cnt += 1
    time = 0
    while cnt:
        next_alive = [[0] * 101 for _ in range(101)]
        next_cnt = 0
        for i in range(1, 101):
            for j in range(1, 101):
                if alive[i][j] + alive[i][j - 1] + alive[i - 1][j] >= 2:
                    next_alive[i][j] = 1
                    next_cnt += 1
        alive, cnt = next_alive, next_cnt
        time += 1
    print(f"Case #{tc}: {time}")