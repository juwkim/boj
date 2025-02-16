hand = []
for card in open(0).read().split():
    hand.append(card)
    removed = True
    while len(hand) >= 4 and removed:
        removed = False
        for i in range(len(hand) - 1, 2, -1):
            if hand[i][0] == hand[i - 3][0]:
                removed = True
                hand = hand[:i - 3] + hand[i + 1:]
                break
        for i in range(len(hand) - 1, 2, -1):
            if hand[i][1] == hand[i - 3][1]:
                removed = True
                hand = hand[:i - 3] + hand[i - 2:i] + hand[i + 1:]
                break
print(len(hand), *hand)