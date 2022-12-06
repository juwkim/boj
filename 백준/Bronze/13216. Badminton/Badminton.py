game = input()
score = [0, 0]
for i in game:
    score[i == 'B'] += 1
    if 21 in score:
        print(f'{score[0]}-{score[1]}')
        score = [0, 0]
print('AB'[game[-1] == 'B'])