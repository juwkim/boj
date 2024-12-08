n = int(input())
ans = -1
for a in range(1, n + 1):
    c, r1 = divmod(n, a)
    if r1:
        continue
    for b in range(1, n + 3):
        d, r2 = divmod(n + 2, b)
        if r2:
            continue
        if -b * c + a * d == n + 1:
            ans = f"{a} {-b} {c} {d}"
            break
        elif b * c - a * d == n + 1:
            ans = f"{a} {b} {c} {-d}"
            break
    if ans != -1:
        break
print(ans)