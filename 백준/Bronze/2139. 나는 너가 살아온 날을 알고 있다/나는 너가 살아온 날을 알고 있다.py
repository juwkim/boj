from datetime import date
while (s:=input()) != '0 0 0':
    d, m, y = map(int, s.split())
    a = date(y, m, d) - date(y, 1, 1)
    print(1 + a.days)