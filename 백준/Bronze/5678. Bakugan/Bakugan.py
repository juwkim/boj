while int(input()):
    mark = [*map(int, input().split())]
    leti = [*map(int, input().split())]
    score_mark, score_leti = 0, 0
    last_mark, last_leti = 0, 0
    acc_mark, acc_leti = 1, 1
    is_scored = 0

    for M, L in zip(mark, leti):
        score_mark += M
        score_leti += L
        if M == last_mark:
            acc_mark += 1
        else:
            acc_mark = 1
        if L == last_leti:
            acc_leti += 1
        else:
            acc_leti = 1

        last_mark, last_leti = M, L
        if not is_scored:
            if acc_mark == 3 and acc_leti == 3:
                is_scored = 1
            elif acc_mark == 3:
                is_scored = 1
                score_mark += 30
            elif acc_leti == 3:
                is_scored = 1
                score_leti += 30

    print('TML'[(score_mark > score_leti) - (score_mark < score_leti)])