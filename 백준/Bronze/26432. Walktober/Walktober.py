def g(): return [*map(int, input().split())]

for t in range(1, 1 + int(input())):
    m, n, p = g()
    ans = 0
    for l in zip(*[g() for _ in range(m)]):
        ans += max(l) - l[p - 1]
    print(f'Case #{t}: {ans}')