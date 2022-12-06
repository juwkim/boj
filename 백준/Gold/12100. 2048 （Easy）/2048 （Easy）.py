from math import log2

def move(N, lst):
    ans = []
    i, len_lst = 0, len(lst)
    now = lst[i]
    i += 1
    change = False
    while i < len_lst and now == 0:
        now = lst[i]
        i += 1
    while i < len_lst:
        new = lst[i]
        i += 1
        if new == 0:
            continue
        elif now == new:
            ans.append(now + new)
            change = True
            now = -1
        elif now == -1:
            now = new
        else:
            ans.append(now)
            now = new
    if now != -1:
        ans.append(now)
    ans += [0] * (N - len(ans))
    return ans, change

def up(board, iteration):
    # global count
    # count += 1
    global g_max
    if g_max == best_max:
        return

    new_board = [[0 for _ in range(N)] for _ in range(N)]
    change_cnt = 0
    for j in range(N):
        moved, change = move(N, [board[i][j] for i in range(N)])
        change_cnt += change
        for i in range(N):
            new_board[i][j] = moved[i]

    iteration += 1
    l_max = max(map(max, new_board))
    # print("board")
    # for line in board:
    #     print(line)
    # print("new board")
    # for line in board:
    #     print(line)
    if l_max == best_max:
        g_max = l_max
        return
    
    if new_board == board or l_max <= check[iteration]:
        return

    if iteration == s:
        if l_max > g_max:
            g_max = l_max
            check[s] = g_max
            for i in range(s, 1, -1):
                check[i-1] = check[i] // 2
        return
    
    up(new_board, iteration)
    if change_cnt:
        down(new_board, iteration)
    else:
        g_max = max(g_max, l_max)
    right(new_board, iteration)
    left(new_board, iteration)

def down(board, iteration):
    # global count
    # count += 1
    global g_max
    if g_max == best_max:
        return
    
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    change_cnt = 0
    for j in range(N):
        moved, change = move(N, [board[i][j] for i in range(N-1, -1, -1)])
        change_cnt += change
        for i in range(N):
            new_board[N-i-1][j] = moved[i]

    iteration += 1
    l_max = max(map(max, new_board))
    # print("board")
    # for line in board:
    #     print(line)
    # print("new board")
    # for line in board:
    #     print(line)
        
    if l_max == best_max:
        g_max = l_max
        return

    
    if new_board == board or l_max <= check[iteration]:
        return

    if iteration == s:
        if l_max > g_max:
            g_max = l_max
            check[s] = g_max
            for i in range(s, 1, -1):
                check[i-1] = check[i] // 2
        return
    if change_cnt:
        up(new_board, iteration)
    else:
        g_max = max(g_max, l_max)
    down(new_board, iteration)
    right(new_board, iteration)
    left(new_board, iteration)

def right(board, iteration):
    # global count
    # count += 1
    global g_max
    if g_max == best_max:
        return

    new_board = [[0 for _ in range(N)] for _ in range(N)]
    change_cnt = 0
    for i in range(N):
        temp, change = move(N, board[i][::-1])
        new_board[i] = temp[::-1]
        change_cnt += change

    iteration += 1
    l_max = max(map(max, new_board))
    # print("board")
    # for line in board:
    #     print(line)
    # print("new board")
    # for line in board:
    #     print(line)
    if l_max == best_max:
        g_max = l_max
        return
    
    if new_board == board or l_max <= check[iteration]:
        return

    if iteration == s:
        if l_max > g_max:
            g_max = l_max
            check[s] = g_max
            for i in range(s, 1, -1):
                check[i-1] = check[i] // 2
        return
    
    up(new_board, iteration)
    down(new_board, iteration)
    right(new_board, iteration)
    if change_cnt:
        left(new_board, iteration)
    else:
        g_max = max(g_max, l_max)

def left(board, iteration):
    # global count
    # count += 1
    global g_max
    if g_max == best_max:
        return
    
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    change_cnt = 0
    for i in range(N):
        new_board[i], change = move(N, board[i])
        change_cnt += change
    
    iteration += 1
    l_max = max(map(max, new_board))
    # print("board")
    # for line in board:
    #     print(line)
    # print("new board")
    # for line in board:
    #     print(line)
    if l_max == best_max:
        g_max = l_max
        return
    
    if new_board == board or l_max <= check[iteration]:
        return

    if iteration == s:
        if l_max > g_max:
            g_max = l_max
            check[s] = g_max
            for i in range(s, 1, -1):
                check[i-1] = check[i] // 2
        return
    
    up(new_board, iteration)
    down(new_board, iteration)
    if change_cnt:
        right(new_board, iteration)
    else:
        g_max = max(g_max, l_max)
    left(new_board, iteration)


N = int(input())
board = [[*map(int, input().split())] for _ in range(N)]
# 기대할 수 있는 가장 큰 수
# 만약 g_max가 이 수에 도달하면, 그 즉시 종료
best_max = pow(2, int(log2(sum(map(sum, board)))))
check = [0 for _ in range(11)]


s = 5
g_max = 0
# count = 0
up(board, 0)
down(board, 0)
right(board, 0)
left(board, 0)
print(g_max)