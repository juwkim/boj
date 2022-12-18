l = [50, 20, 10, 5, 1]
for _ in range(int(input())):
    a, b = map(float, input().split())
    money = b - a
    buf = []
    for c in l:
        q, money = divmod(money, c)
        buf.append(int(q))
    tmp = []
    for i, j in zip(buf, l):
        tmp.append(f'{i}-${j}')
    print(', '.join(tmp))