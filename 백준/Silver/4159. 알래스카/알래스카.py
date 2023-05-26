while N := int(input()):
    pos = sorted(int(input()) for _ in range(N))
    if pos[-1] >= 1322 and all(b - a <= 200 for a, b in zip(pos, pos[1:])):
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')