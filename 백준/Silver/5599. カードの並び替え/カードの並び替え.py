n = int(input())
cards = [*range(1, 1 + 2 * n)]
for _ in range(int(input())):
    op = int(input())
    if op == 0:
        top = cards[:n]
        btm = cards[n:]
        cards = []
        for i in range(n):
            cards.append(top[i])
            cards.append(btm[i])
    else:
        cards = cards[op:] + cards[:op]
print(*cards)