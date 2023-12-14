import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def solve(idx):
    global diff, owner_max
    if idx == t:
        val = [0] * h
        for product_idx, owner_idx in enumerate(owner):
            val[owner_idx] += treasure[owner_idx][product_idx]
        new_diff = max(val) - min(val)
        if new_diff < diff:
            diff = new_diff
            owner_max = owner[:]
        return
    for i in range(h):
        owner[idx] = i
        solve(idx + 1)

while True:
    try:
        input()
        t, h = int(input()), int(input())
        treasure = [g() for _ in range(h)]
        owner = [-1] * t
        owner_max = [-1] * t
        diff = float('inf')
        solve(0)
        product = [[] for _ in range(h)]
        for i in range(t):
            product[owner_max[i]].append(i)
        for i in range(h):
            print(*[p + 1 for p in product[i]], sum(treasure[i][j] for j in product[i]))
        print()
        input()
    except:
        break