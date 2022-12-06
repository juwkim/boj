from decimal import Decimal, getcontext, ROUND_HALF_UP
getcontext().rounding = ROUND_HALF_UP
g = lambda: [*map(int, input().split())]

n, m = g()
res = [[0, i, input()] for i in range(n)]
invalid = 0
for _ in range(m):
    vote = input()
    idx = [i for i in range(n) if vote[i] == 'X']
    if len(idx) == 1:
        res[idx[0]][0] -= 1
    else:
        invalid += 1
res.sort()
m = Decimal(m)
for score, _, name in res:
    p = (- score * 100) / m
    print(f'{name} {p:.2f}%')
p = (invalid * 100) / m
print(f'Invalid {p:.2f}%')