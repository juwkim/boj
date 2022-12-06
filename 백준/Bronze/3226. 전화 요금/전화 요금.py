cnt = 0
for _ in range(int(input())):
    time, due = input().split()
    due = int(due)
    h, m = map(int, time.split(':'))
    start = h * 60 + m
    if 420 <= start <= 1140:
        if start + due <= 1140:
            cnt += 10 * due
        else:
            a = 1140 - start
            cnt += 10 * a + 5 * (due - a)
    else:
        if start <= 420 <= start + due:
            a = 420 - start
            cnt += 5 * a + 10 * (due - a)
        else:
            cnt += 5 * due
print(cnt)