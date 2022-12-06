while (game:= input()) != '#':
    win = [0, 0]
    score = [0, 0]
    for point in game:
        score[point == 'B'] += 1
        if max(score) >= 4 and abs(score[0] - score[1]) >= 2:
            win[max(score) == score[1]] += 1
            score = [0, 0]
    print(f'A {win[0]} B {win[1]}')