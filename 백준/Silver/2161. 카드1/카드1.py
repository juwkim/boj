card = [*range(1, 1+int(input()))]
discarded = []
while len(card) != 1:
    discarded.append(card.pop(0))
    card.append(card.pop(0))
print(*discarded, *card)