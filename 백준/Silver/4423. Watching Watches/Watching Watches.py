import sys
input = lambda: sys.stdin.readline().rstrip()
while True:
    try:
        p = input()
        a, b = sorted(map(int, p.split()))
        s = ((86400 - a) * 43200 + 30 * (b - a)) // (b - a)
        h, s = divmod(s % 43200, 3600)
        m = s // 60
        if h == 0: h = 12
        print(f'{p} {h:02d}:{m:02d}')
    except:
        break