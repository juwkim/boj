import sys
input = lambda: sys.stdin.readline().rstrip()

while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    board = input()
    deck = [input() for _ in range(c)]
    winner, pos = None, [-1] * a
    i = 0
    while i < c:
        p = i % a
        card = deck[i]
        cur, idx = pos[p] + 1, 0
        while cur < b:
            if board[cur] == card[idx]:
                idx += 1
                if idx == len(card):
                    break
            cur += 1
        i += 1
        if cur >= b - 1:
            winner = p + 1
            break
        pos[p] = cur
    if winner:
        print(f"Player {winner} won after {i} cards.")
    else:
        print(f"No player won after {c} cards.")