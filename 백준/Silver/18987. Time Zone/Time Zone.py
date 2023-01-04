input = __import__('sys').stdin.readline
for _ in range(int(input())):
    *l, s = input().split()
    a, b = map(int, l)
    minutes = (a - 8) * 60 + b
    if '.' in s:
        p, q = map(int, s[4:].split('.'))
        if s[3] == '+':
            minutes += p * 60 + q * 6
        else:
            minutes -= p * 60 + q * 6
    else:
        minutes += int(s[3:]) * 60
    h, m = divmod(minutes % 1440, 60)
    print(f'{h:02d}:{m:02d}')