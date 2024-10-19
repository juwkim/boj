win_a, win_b = 0, 0
power_a, power_b = 0, 0

def solve(location, cards):
    card_power = {
        "Shadow": 6,
        "Gale": 5,
        "Ranger": 4,
        "Anvil": 7,
        "Vexia": 3,
        "Guardian": 8,
        "Frostwhisper": 2,
        "Voidclaw": 3,
        "Ironwood": 3,
        "Thunderheart": (6, 12)[len(cards) == 4],
        "Zenith": (4, 9)[location == 1],
        "Seraphina": len(cards)
    }
    return sum(card_power[card] for card in cards)

for i in range(3):    
    na, *a_cards = input().split()
    nb, *b_cards = input().split()
    pa, pb = solve(i, a_cards), solve(i, b_cards)
    if pa > pb:
        win_a += 1
    elif pa < pb:
        win_b += 1
    power_a += pa
    power_b += pb

if win_a > win_b:
    print("Player 1")
elif win_a < win_b:
    print("Player 2")
elif power_a > power_b:
    print("Player 1")
elif power_a < power_b:
    print("Player 2")
else:
    print("Tie")