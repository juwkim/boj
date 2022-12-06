for _ in range(int(input())):
    l1, a1, l2, a2, lt, at = map(int, input().split())
    rec = []
    for x in range(1, (lt - l2) // l1 + 1):
        y = (lt - l1 * x) / l2
        if y == int(y) and a1 * x + a2 * y == at:
            rec += [[x, int(y)]]
    print(*rec[0] if len(rec) == 1 else '?')