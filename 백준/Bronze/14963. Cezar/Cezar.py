deck = [4 for _ in range(8)] + [16, 4]
num = 21

for _ in range(int(input())):
    card = int(input())
    num -= card
    deck[card - 2] -= 1

if num > 10:
    print('VUCI')
elif num > 2:
    print(['DOSTA', 'VUCI'][sum(deck[num-1:]) < sum(deck[:num-1])])
else:
    print('DOSTA')