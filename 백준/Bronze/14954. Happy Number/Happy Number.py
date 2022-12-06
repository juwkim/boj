n = int(input())
t, res = n, []
while True:
    t = sum(map(lambda x: int(x)**2, str(t)))
    if t == 1:
        print('HAPPY')
        break
    if t in res:
        print('UNHAPPY')
        break
    res += [t]