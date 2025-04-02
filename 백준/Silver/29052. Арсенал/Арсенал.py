n = int(input())
a = sorted(enumerate(map(int, input().split()), 1), key=lambda x: (x[1], x[0]), reverse=True)
ans, l = 0, []
pidx, prv, cur = -1, 0, 1
for i in range(n):
    if a[i] == (pidx - 1, prv):
        cur += 1
    else:
        l.extend(range(pidx + 1, pidx + cur, 2))
        l.extend(range(pidx, pidx + cur, 2))
        ans += cur >> 1
        cur = 1
    pidx, prv = a[i]
l.extend(range(pidx + 1, pidx + cur, 2))
l.extend(range(pidx, pidx + cur, 2))
ans += cur >> 1
print(ans)
print(*l[1:])