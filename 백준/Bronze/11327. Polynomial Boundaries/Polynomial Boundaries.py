while (s:=input()) != '0':
    s = [*map(int, s.split())]
    x, y = map(int, input().split())
    t = sum(s[i+1] * x ** i for i in range(s[0]))
    print(['On', 'Outside', 'Inside'][(y > t) - (y < t)])