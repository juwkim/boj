g = lambda: [*map(int, input().split())]

n, m = g()
p = [0] + g()
ans = [0]
good = True
for i in range(1, n + 1):
    if p[i] == -1:
        ans.append(m)
        p[i] = p[i - 1] + m
    elif p[i] - p[i - 1] >= m:
        ans.append(p[i] - p[i - 1])
    else:
        good = False
        break
if good:
    print(*ans[1:])
else:
    print(-1)