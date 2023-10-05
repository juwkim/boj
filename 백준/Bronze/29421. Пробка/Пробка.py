import sys
input = lambda: sys.stdin.readline().rstrip()

n, g, r = [*map(int, input().split())]
cur, left = 0, g
for num in map(int, input().split()):
    if left >= num:
        cur += num
        left -= num
    else:
        cur += left + r + num
        left = g - num
print(cur)