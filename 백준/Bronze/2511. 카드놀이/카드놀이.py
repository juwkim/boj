A = [*map(int, input().split())]
B = [*map(int, input().split())]
score_A, score_B, last_win = 0, 0, 'D'
for x, y in zip(A, B):
    if x > y:
        score_A += 3
        last_win = 'A'
    elif x < y:
        score_B += 3
        last_win = 'B'
    else:
        score_A += 1
        score_B += 1
if score_A == score_B:
    print(f'{score_A} {score_B}\n{last_win}')
else:
    winner = 'B'
    if score_A > score_B:
        winner = 'A'
    print(f'{score_A} {score_B}\n{winner}')