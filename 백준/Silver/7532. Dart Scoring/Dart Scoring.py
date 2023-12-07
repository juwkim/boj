import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

game = []
buf = open(0).read().replace('\n', '').split(',')
l = []
for dart in buf:
    if dart == '#':
        if l:
            game.append(l)
            l = []
    else:
        l.append(dart)

for round, darts in enumerate(game, 1):
    print(f"Game {round}")
    print("  301  301")
    score = [301, 301]
    started = [False, False]
    cur = [0, 0]
    turn, cnt = 0, 3
    winner = None
    for dart in darts:
        if dart == 'M':
            pass
        elif dart == 'OB':
            if started[turn]:
                cur[turn] += 25
        elif dart == 'B':
            started[turn] = True
            cur[turn] += 50
        elif dart[0] == 'S':
            if started[turn]:
                cur[turn] += int(dart[1:])
        elif dart[0] == 'D':
            started[turn] = True
            cur[turn] += int(dart[1:]) * 2
        elif dart[0] == 'T':
            if started[turn]:
                cur[turn] += int(dart[1:]) * 3
        if cur[turn] == score[turn] and (dart == "B" or dart[0] == "D"):
            winner = turn
            break
        cnt -= 1
        if cnt == 0:
            if cur[turn] + 2 <= score[turn]:
                score[turn] -= cur[turn]
            if turn & 1:
                print(f"{score[0]:5}{score[1]:5}")
                cur = [0, 0]
            cnt = 3
            turn ^= 1
        elif cur[turn] + 2 > score[turn]:
            if turn & 1:
                print(f"{score[0]:5}{score[1]:5}")
                cur = [0, 0]
            cnt = 3
            turn ^= 1
    if winner == 0:
        print(f" Wins{score[1]:5}")
    elif winner == 1:
        print(f"{score[0]:5} Wins")
    print()