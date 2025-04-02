used_cards = set()
prohibited_colors = [set() for _ in range(5)]
starter, paradoxes = 0, []
for round in range(1, int(input()) + 1):
    cards = input().split()
    round_color = cards[0][0]
    winner = -1, -1
    for idx, (color, number) in enumerate(cards, starter):
        idx %= 5
        if (color, number) in used_cards or color in prohibited_colors[idx]:
            paradoxes.append((round, idx))
            continue
        if color != round_color: prohibited_colors[idx].add(round_color)
        used_cards.add((color, number))
        winner = max(winner, ((0, 100, 10)[(color == 'C') - (color != 'C' and color == round_color)] + int(number), idx))
    starter = winner[1]
players = "SONJA", "VIKTOR", "IGOR", "LEA", "MARINO"
print(len(paradoxes))
for round, idx in paradoxes:
    print(round, players[idx])