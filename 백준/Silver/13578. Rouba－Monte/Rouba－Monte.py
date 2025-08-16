import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

while True:
    n, j = g()
    if n == 0:
        break
    deck = g()[::-1]
    discard = [0] * 14
    top = [None] * j
    size = [0] * j
    p = 0
    while deck:
        while deck:
            v = deck.pop()
            if discard[v]:
                discard[v] -= 1
                size[p] += 2
                top[p] = v
                continue

            steal = -1
            for q in range(j):
                if q == p:
                    continue
                if top[q] == v:
                    steal = q
                    break
            if steal != -1:
                q = steal
                size[p] += size[q] + 1
                size[q] = 0
                top[p] = v
                top[q] = None
                continue

            if top[p] == v:
                size[p] += 1
                top[p] = v
                continue
            discard[v] += 1
            break
        p = (p + 1) % j
    Max = max(size)
    print(Max, *[i for i, c in enumerate(size, 1) if c == Max])