from itertools import combinations
from collections import Counter

def is_straight(ranks):
    a = min(ranks)
    return sorted(ranks) == [a, a + 1, a + 2, a + 3, a + 4]

def classify(hand):
    ranks, suits = zip(*hand)
    rc = Counter(ranks)
    sc = Counter(suits)
    flush = 5 in sc.values()
    straight = is_straight(ranks)
    if flush and straight:
        return 0
    if 4 in rc.values():
        return 1
    if sorted(rc.values()) == [2, 3]:
        return 2
    if flush:
        return 3
    if straight:
        return 4
    if 3 in rc.values():
        return 5
    if Counter(rc.values())[2] == 2:
        return 6
    if 2 in rc.values():
        return 7
    return 8

A, B, a1, b1, a2, b2 = map(int, open(0).read().split())
base = [(a1, b1), (a2, b2)]
deck = [(r, s) for r in range(A) for s in range(B)
        if (r, s) not in base]
cnt = [0] * 9
for c in map(list, combinations(deck, 3)):
    cnt[classify(base + c)] += 1
print(*cnt)