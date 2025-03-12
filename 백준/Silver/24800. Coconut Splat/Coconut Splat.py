from collections import deque

s, n = map(int, input().split())
coconuts = deque([(i, 1) for i in range(n)])
idx = 0
while len(coconuts) > 1:
    idx = (idx + s - 1) % len(coconuts)
    player, state = coconuts[idx]
    if state == 1:  # Folded
        coconuts[idx] = (player, 2)
        coconuts.insert(idx + 1, (player, 2))
    elif state == 2:  # Fist
        coconuts[idx] = (player, 3)
        idx += 1
    else:  # Palm down
        coconuts.remove((player, state))
print(coconuts[0][0] + 1)