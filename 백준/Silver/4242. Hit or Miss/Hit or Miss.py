from collections import deque

def hash(players, counts):
    return tuple(tuple(p) for p in players), tuple(counts)

for tc in range(1, int(input()) + 1):
    n, *cards = map(int, input().split())
    players = [deque(cards)] + [deque() for _ in range(n - 1)]
    counts = [0] * n
    discard = [0] * n
    states = {hash(players, counts)}
    while True:
        passed = [0] * (n + 1)
        for i in range(n):
            if not players[i]:
                continue
            card = players[i].popleft()
            if card == counts[i] + 1:
                discard[i] = card
                passed[i+1] = card
            else:
                players[i].append(card)
            counts[i] = (counts[i] + 1) % 13
        for i in range(1, n):
            if passed[i]:
                players[i].append(passed[i])
        if all(len(p) == 0 for p in players):
            ans = " ".join(str(x) for x in discard)
            break
        state = hash(players, counts)
        if state in states:
            ans = "unwinnable"
            break
        states.add(state)
    print(f"Case {tc}: {ans}")