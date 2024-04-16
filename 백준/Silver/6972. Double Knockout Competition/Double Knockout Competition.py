n = int(input())
for _ in range(n):
    a, b, c, r = int(input()), 0, 0, 0
    print(f"Round 0: {a} undefeated, 0 one-loss, 0 eliminated")
    while (a, b) != (0, 1):
        r += 1
        if (a, b) == (1, 1):
            a, b = 0, 2
        else:
            cnt = b >> 1
            b -= cnt; c += cnt
            cnt = a >> 1
            b += cnt; a -= cnt
        print(f"Round {r}: {a} undefeated, {b} one-loss, {c} eliminated")
    print(f"There are {r} rounds{('.','')[n == 1]}\n")