from datetime import date
for _ in range(3):
    s = input()
    try:
        d, m, y = map(int, [s[:2], s[2:4], s[4:7]])
        y += 1000 * (1 + (y < 600))
        date(y, m, d)
        if s[7] not in '169':
            print(0)
        else:
            print(+(int(s[8]) == sum(int(s[i])**2 for i in range(8)) % 7))
    except:
        print(0)