def g(): return [*map(int, input().split())]

n, m = g()
fishes = sorted(g())
fishmongers = sorted([g() for _ in range(m)], key=lambda x: -x[1])

ans = 0
for x, p in fishmongers:
    while x and fishes:
        ans += fishes.pop() * p
        x -= 1
    if not fishes:
        break
print(ans)