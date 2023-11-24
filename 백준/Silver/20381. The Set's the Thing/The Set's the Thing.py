from itertools import combinations

for cards in map(str.split, open(0).read().split("\n\n")):
    sets = [l for l in combinations(cards, 3) if all(len(set(x)) != 2 for x in zip(*l))]
    print("CARDS: ", *cards)
    if sets:
        a, b, c = sets[0]
        print(f"SETS:   1.  {a} {b} {c}")
        for i, (a, b, c) in enumerate(sets[1:], 2):
            print(" " * 8 + f"{i}." + " " * (3 - len(str(i))) + f"{a} {b} {c}")
    else:
        print("SETS:   *** None Found ***")
    print()