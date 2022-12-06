N, B = input().split()
score = 0
table = {'A': 11, 'K': 4, 'Q': 3, 'J': 2,
         'T': 10, '9': 0, '8': 0, '7': 0}
for _ in range(4*int(N)):
    card = input()
    score += table[card[0]]
    if card[0] == 'J' and card[1] == B:
        score += 18
    if card[0] == '9' and card[1] == B:
        score += 14
print(score)