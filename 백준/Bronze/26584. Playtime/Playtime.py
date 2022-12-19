l = ['year(s)', 'day(s)', 'hour(s)', 'minute(s)']
for _ in range(int(input())):
    game, m = input().split(',')
    m = int(m)
    print(game, '-', end=' ')
    for idx, num in enumerate((525600, 1440, 60, 1)):
        q, m = divmod(m, num)
        if q:
            print(q, l[idx], end=' ')
    print()