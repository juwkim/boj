import sys
from datetime import date, timedelta
input = lambda: sys.stdin.readline().rstrip()

input()
check = set(input())
check.add('-')

d1, m1, y1 = map(int, input().split('.'))
d2, m2, y2 = map(int, input().split('.'))

a1 = date(y1, m1, d1)
a2 = date(y2, m2, d2)
ans = 0
while True:
    ans += set(a1.isoformat()).issubset(check)
    if a1 == a2:
        break
    a1 += timedelta(days=1)
print(ans)