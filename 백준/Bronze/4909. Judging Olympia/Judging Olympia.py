while True:
    score = sorted(map(int, input().split()))
    if score == [0, 0, 0, 0, 0, 0]:
        break
    print(str(sum(score[1:-1]) / 4).replace('.0', ''))