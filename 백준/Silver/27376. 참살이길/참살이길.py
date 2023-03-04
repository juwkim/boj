g = lambda: map(int, input().split())

n, k = g()
pos, time = 0, 0
for x, t, s in sorted(tuple(g()) for _ in range(k)):
    time += x - pos
    pos = x
    if time < s:
        time += s - time
    else:
        left = (time - s) % (2 * t)
        if left >= t:
            time += max(0, 2 * t - left)

time += n - pos
print(time)