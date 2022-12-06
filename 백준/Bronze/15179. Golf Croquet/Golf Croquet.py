t1, t2 = input(), input()
n = int(input())
game = input()
score = [0, 0]
for i in range(len(game)):
    if game[i] == 'H':
        score[i%2] += 1
    elif game[i] == 'D':
        score[i%2] = min(7, 2 + score[i%2])
    elif game[i] == 'O':
        score[1 - i%2] += 1
    if 7 in score:
        break
s1, s2 = score
print(t1, s1, t2, s2, end='. ')
if s1 == 7:
    print(f'{t1} has won.')
elif s2 == 7:
    print(f'{t2} has won.')
elif s1 > s2:
    print(f'{t1} is winning.')
elif s1 < s2:
    print(f'{t2} is winning.')
else:
    print('All square.')