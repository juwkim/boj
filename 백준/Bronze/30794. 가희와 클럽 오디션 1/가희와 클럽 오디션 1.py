import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

lv, what = input().split()

if what == 'miss':
    ans = 0
elif what == 'bad':
    ans = 200
elif what == 'cool':
    ans = 400
elif what == 'great':
    ans = 600
else:
    ans = 1000
ans *= int(lv)
print(ans)