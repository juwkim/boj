g = lambda: [*map(int, input().split())]

while (s:= input()) != '0 0':
    a = min(g())
    b = sorted(g())[1]
    print('NY'[a < b])