L, x = map(int, input().split())
now, count = 0, 0
for _ in range(x):
    s, t = input().split()
    t = int(t)
    if s == 'enter':
        if t > L - now:
            count += 1
        else:
            now += t
    if s == 'leave':
        now -= t
print(count)