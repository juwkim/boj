s = "?15??2??8?"
g = lambda: [*map(int, input().split())]
W, N = input().split()
Map = [g() for _ in range(int(N))]
if W in 'LR':
    for line in Map:
        print(*[s[i] for i in line[::-1]])
else:
    Map = Map[::-1]
    for line in Map:
        print(*[s[i] for i in line])  