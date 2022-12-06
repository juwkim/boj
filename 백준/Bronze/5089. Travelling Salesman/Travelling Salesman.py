i = 1
while (n:=int(input())):
    print('Week', i, len({input() for _ in range(n)}))
    i += 1