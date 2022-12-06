import sys
input = sys.stdin.readline
from datetime import date

# retrun 2 if valid day and safe
# return 1 if valid day and not safe
# return 0 if not valid

Y, M, D = map(int, input().split())
base = date(2000 + Y, M, D)
l = ('invalid', 'unsafe', 'safe')
for _ in range(int(input())):
    A, B, C = map(int, input().split())
    Sum = 0
    for a, b, c in ((A, B, C), (C, B, A), (C, A, B)):
        try:
            Sum += 1 + ((date(2000 + a, b, c) - base).days >= 0)
        except:
            pass
        if Sum & 1:
            break
    print(l[(Sum & 1) or ((Sum > 0) * 2)])