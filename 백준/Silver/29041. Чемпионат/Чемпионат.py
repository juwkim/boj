g = lambda: [*map(int, input().split())]

n, m = g()
a = g()
b = g()
ans, buf = "YES", []
while True:
    i = max(range(n), key=lambda x: a[x])
    j = max(range(m), key=lambda x: b[x])
    if a[i] == 0 or b[j] == 0:
        break
    if a[i] > b[j]:
        for k in sorted(range(m), key=lambda x: b[x], reverse=True)[:a[i]]:
            if b[k] == 0:
                break
            a[i] -= 1
            b[k] -= 1
            buf.append((i + 1, k + 1))
        if a[i]:
            ans = "NO"
            break
    else:
        for k in sorted(range(n), key=lambda x: a[x], reverse=True)[:b[j]]:
            if a[k] == 0:
                break
            a[k] -= 1
            b[j] -= 1
            buf.append((k + 1, j + 1))
        if b[j]:
            ans = "NO"
            break
print(ans)
if ans == "YES":
    print(len(buf))
    for i, j in buf:
        print(i, j)