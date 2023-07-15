def get_WP(i):
    win, lose = 0, 0
    for c in board[i]:
        if c == '1':
            win += 1
        elif c == '0':
            lose += 1
    return win / (win + lose)

def get_OWP(i):
    l = []
    for op in range(N):
        if board[i][op] == '.':
            continue
        win, lose = 0, 0
        for j in range(N):
            if i == j:
                continue
            c = board[op][j]
            if c == '1':
                win += 1
            elif c == '0':
                lose += 1
        l.append(win / (win + lose))
    return sum(l) / len(l)

def get_OOWP(i):
    l = []
    for op in range(N):
        if board[i][op] == '.':
            continue
        l.append(OWP_list[op])
    return sum(l) / len(l)

for tc in range(1, 1 + int(input())):
    N = int(input())
    board = [input() for _ in range(N)]
    
    print(f"Case #{tc}:")
    OWP_list = [get_OWP(i) for i in range(N)]
    for i in range(N):
        WP = get_WP(i)
        OWP = OWP_list[i]
        OOWP = get_OOWP(i)
        RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
        print(RPI)