g = lambda: list(map(int, input().split()))
mod = 10 ** 9 + 7
D = int(input())
cur, sibling, fac = 0, 0, 1
for generation, num in enumerate(g()):
    cur = (cur + sibling * generation - 1 + num + fac) % mod
    sibling = sibling * (generation + 1) + num - 1
    fac *= (generation + 1)
    print(cur)