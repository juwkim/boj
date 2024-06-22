M, *p = map(int, open(0))
p = set(p)
ans = 100
for N in range(1, 100):
    s = {(i * 100 + N // 2) // N for i in range(N + 1)}
    if p.issubset(s):
        ans = N
        break
print(ans)