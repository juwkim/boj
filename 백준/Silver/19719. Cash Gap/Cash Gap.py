g = lambda: [*map(int, input().split())]

n, m, s = g()
add = [0] * m
sub = [0] * m
for _ in range(n):
    count, From, To = g()
    if count > 0:
        add[To - 1] += count
    elif count < 0:
        sub[From - 1] += count

ans = 'NO'
for a, b in zip(sub, add):
    if s + a < 0:
        ans = 'YES'
        break
    s += a + b
print(ans)