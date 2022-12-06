score = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'K': 10, 'Q': 10, 'J': 10, 'T': 10, 'A': 11}
while N:= int(input()):
    deck = {card: 4 * N for card in '23456789TAKQJ'}
    l = input().split()
    for card in l:
        deck[card] -= 1
    
    total = 52 * N - 3
    
    D, S1, S2 = l
    if S1 == S2 == 'A':
        player = 12
    else:
        player = score[S1] + score[S2]
    
    win = 0
    dealer = score[D]
    for card in deck:
        if card == 'A' and dealer == 11:
            num = 12
        else:
            num = dealer + score[card]
        if player > num:
            win += deck[card]
    print(f'{win * 100 / total:.3f}%')