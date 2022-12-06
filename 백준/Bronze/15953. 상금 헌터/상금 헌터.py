f = {0: 0, 1: 500, 2: 300, 3: 200, 4: 50, 5: 30, 6: 10}
g = {0: 0, 1: 512, 2: 256, 3: 128, 4: 64, 5: 32}
for _ in range(int(input())):
    a, b = map(int, input().split())
    s, t, money = 0, 0, 0
    while a > s*(s+1)//2:
        s += 1
    while b > 2**t - 1:
        t += 1
    if s in f:
        money += f[s]
    if t in g:
        money += g[t]
    print(money * 10000)