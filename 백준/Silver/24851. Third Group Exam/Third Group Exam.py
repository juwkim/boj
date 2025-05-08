g = lambda: map(int, input().split())

n, a, b = g()
ans = [''] * n
total = 0
count_t, count_p = 0, 0
for i, (x, y) in sorted([(i, p) for i, p in enumerate(zip(g(), g()))], key=lambda x: -abs(x[1][0] - x[1][1])):
    if n - count_p == a or (n - count_t != b and x > y):
        ans[i] = 'T'
        count_t += 1
        total += x
    else:
        ans[i] = 'P'
        count_p += 1
        total += y
print(total)
print(*ans)