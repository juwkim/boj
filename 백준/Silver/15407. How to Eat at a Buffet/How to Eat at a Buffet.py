g = lambda: [*map(int, input().split())]

n, a = int(input()), int(input())
foods = sorted([g() for _ in range(n)], reverse=True)

ans = 0
for vi, ai in foods:
    cur = min(a, ai)
    a -= cur
    ans += vi * cur
    if a == 0:
        break
print(ans)