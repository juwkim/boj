import sys
input = lambda: sys.stdin.readline().rstrip()

suit_order = {'C': 0, 'D': 1, 'S': 2, 'H': 3}
rank_order = {c: i for i, c in enumerate("23456789TJQKA")}
while (dealer:= input()) != "#":
    deck = input() + input()
    hands = [[] for _ in range(4)]
    dealer_idx = 'SWNE'.index(dealer)
    start = (dealer_idx + 1) % 4
    for i in range(0, 104, 2):
        hands[start].append(deck[i:i+2])
        start = (start + 1) % 4
    for p, name in enumerate(("South", "West", "North", "East")):
        hands[p].sort(key=lambda card: (suit_order[card[0]], rank_order[card[1]]))
        print(f"{name} player:")
        print("+---+---+---+---+---+---+---+---+---+---+---+---+---+")
        for suit, rank in hands[p]: print(f"|{rank} {rank}", end="")
        print("|")
        for suit, rank in hands[p]: print(f"| {suit} ", end="")
        print("|")
        for suit, rank in hands[p]: print(f"|{rank} {rank}", end="")
        print("|")
        print("+---+---+---+---+---+---+---+---+---+---+---+---+---+")
    print()