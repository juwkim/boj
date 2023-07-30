g = lambda: [*map(int, input().split())]

def go_straight():
    global time, head_i, head_j, tail_i, tail_j
    time += 1
    new_i, new_j = (head_i + di[d]) % R, (head_j + dj[d]) % C
    if Map[new_i][new_j] >= 2:
        return False
    if Map[new_i][new_j] <= 0:
        Map[tail_i][tail_j] = 0
        p, q = min(zip(di, dj), key=lambda x: (Map[(tail_i + x[0]) % R][(tail_j + x[1]) % C] <= 1, Map[(tail_i + x[0]) % R][(tail_j + x[1]) % C]))
        tail_i, tail_j = (tail_i + p) % R, (tail_j + q) % C
        Map[tail_i][tail_j] = -1
    head_i, head_j = new_i, new_j
    Map[head_i][head_j] = time
    return True

di, dj = (0, -1, 0, 1), (1, 0, -1, 0)
for tc in range(1, 1 + int(input())):
    S, R, C = g()
    Map = [[i + j & 1 for j in range(C)] for i in range(R)]
    head_i, head_j = 0, 0
    tail_i, tail_j = 0, 0
    Map[tail_i][tail_j] = -1
    d, time = 0, 1
    res = True
    for _ in range(S):
        X, A = input().split()
        X = int(X)
        while time <= X and res:
            res = go_straight()
        if res == False:
            for i in range(S - 1 - _):
                input()
            break
        d = (d + (-1, 1)[A == 'L']) % 4

    for _ in range(max(R, C)):
        res = go_straight()
        if res == False:
            break
    ans = sum(sum([num >= 2 or num == -1 for num in line]) for line in Map)
    print(f"Case #{tc}: {ans}")