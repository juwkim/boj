input()
score, bonus = 0, 0
for i, ans in enumerate(input()):
    if ans == 'O':
        score += i+1+bonus
        bonus += 1
    else:
        bonus = 0
print(score)