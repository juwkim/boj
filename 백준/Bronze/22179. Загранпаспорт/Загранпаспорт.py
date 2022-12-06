flag = 'Yes'
h, m = map(int, input().split(':'))
cur = h * 60 + m
for _ in range(int(input())):
    s, e, d = input().split()
    h1, m1 = map(int, s.split(':'))
    h2, m2 = map(int, e.split(':'))
    t1 = max(h1 * 60 + m1, cur) + int(d)
    t2 = h2 * 60 + m2
    if t1 <= t2:
        cur = t1
    else:
        flag = 'No'
        break
print(flag)
if flag == 'Yes':
    h, m = divmod(cur, 60)
    print(f'{h:02d}:{m:02d}')