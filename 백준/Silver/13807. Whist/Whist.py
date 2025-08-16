import sys
input = lambda: sys.stdin.readline().rstrip()

def rank(c):
    if c.isdigit():
        return int(c)
    return "TJQKA".index(c) + 10

while (trump := input()) != '#':
    ns_tricks, ew_tricks = -6, -6
    leader = 0
    for cards in zip(*[input().split() for _ in range(4)]):
        lead_suit = cards[leader][1]
        has_trump = any(c[1] == trump for c in cards)
        cur = -1, None
        for p in range(4):
            if cards[p][1] == (lead_suit, trump)[has_trump]:
                cur = max(cur, (rank(cards[p][0]), p))

        if cur[1] in (0, 2):
            ns_tricks += 1
        else:
            ew_tricks += 1
        leader = cur[1]
    if ns_tricks > ew_tricks:
        print(f"NS {ns_tricks}")
    else:
        print(f"EW {ew_tricks}")