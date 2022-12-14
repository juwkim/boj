for k in range(1, 1 + int(input())):
    g, t = map(int, input().split())
    print(f'Team #{k}\nGames: {g}\nPoints: {t}\nPossible records:')
    w, t = divmod(t, 3)
    l = g - w - t
    while w >= 0 and l >= 0:
        print(w, t, l, sep='-')
        w -= 1
        t += 3
        l -= 2
    print()