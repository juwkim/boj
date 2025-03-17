import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for tc in range(1, 1 + int(input())):
    t = int(input())
    l = input().split()
    score = [0, 0]
    idx, serve_team = 0, l[0] >= '7'
    while idx < t:
        if serve_team ^ (int(l[idx]) >= 7):
            break
        idx += 1
        touch, last_touch_team, after_serve = 1, serve_team, True
        while idx < t:
            if l[idx] == 'A':
                winner = 1
                idx += 1
                break
            elif l[idx] == 'B':
                winner = 0
                idx += 1
                break
            elif l[idx] == 'X':
                winner = last_touch_team ^ 1
                idx += 1
                break
            player = int(l[idx])
            if last_touch_team ^ (player >= 7):
                last_touch_team ^= 1
                touch = 1
                idx += 1
            else:
                touch += 1
                if touch >= 4 or after_serve and (serve_team ^ (player <= 6)) or l[idx - 1] == l[idx]:
                    winner = last_touch_team ^ 1
                    idx += 1
                    break
                idx += 1
            after_serve = False
        if winner is not None:
            score[winner] += 1
            winner = None
            serve_team ^= 1
    else:
        print(f"Data Set {tc}:\n{score[0]} {score[1]}\n")
        continue
    print(f"Data Set {tc}:\nWrong Serve\n")