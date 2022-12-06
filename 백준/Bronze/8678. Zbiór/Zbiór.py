import sys
I = sys.stdin.readline
for _ in range(int(I())):
    a, b = map(int, I().split())
    print('NIE' if b%a else 'TAK')