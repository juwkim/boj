import sys
h, m, s = map(int, input().split())
t = h*3600 + m*60 + s
for _ in range(int(input())):
    q = sys.stdin.readline().split()
    if q[0] == '1':
        t = (t + int(q[1])) % 86400
    elif q[0] == '2':
        t = (t - int(q[1])) % 86400
    else:
        print(f'{t//3600} {t%3600//60} {t%3600%60}')