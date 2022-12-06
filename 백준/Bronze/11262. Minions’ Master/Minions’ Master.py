g = lambda: [*map(int, input().split())]

import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

for _ in range(int(input())):
    N, *l = g()
    N = decimal.Decimal(N)
    m = decimal.Decimal(sum(l)) / N
    ans = decimal.Decimal(sum(i > m for i in l) * 100) / N
    print(f'{m:.3f} {ans:.3f}%')