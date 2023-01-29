def get_minutes(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

a1, a2 = get_minutes(input()), get_minutes(input())
b1, b2 = get_minutes(input()), get_minutes(input())

ans = 'Never'
for t1 in range(b2):
    t2, r = divmod(a1 - a2 + b1 * t1, b2)
    if t2 > 0 and r == 0:
        ans = t1
        break
if ans == 'Never':
    print('Never')
else:
    day, time = divmod(a1 + b1 * ans, 1440)
    print(["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][day % 7])
    h, m = divmod(time, 60)
    print("%02d:%02d" % (h, m))