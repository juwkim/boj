import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def get_minutes():
    h, m = map(int, input().split(':'))
    return h * 60 + m

a1, a2 = get_minutes(), get_minutes()
b1, b2 = get_minutes(), get_minutes()

ans = 'Never'
for t1 in range(1, 1441):
    t2, r = divmod(a1 - a2 + b1 * t1, b2)
    if t2 >= 0 and r == 0:
        ans = t1
        break
if ans == 'Never':
    print('Never')
else:
    day, time = divmod(a1 + b1 * ans, 1440)
    print(["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][day % 7])
    print("%02d:%02d" % divmod(time, 60))