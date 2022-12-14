g = lambda: [*map(int, input().split())]

n, m = g()
good = sorted([int(input()) for _ in range(n)], reverse=True)
bad = sorted([int(input()) for _ in range(m)], reverse=True)
ans, i = n, 0
for num in bad:
    if good[i] > num:
        ans += 1
        i += 1
        if i == n:
            break
print(ans)