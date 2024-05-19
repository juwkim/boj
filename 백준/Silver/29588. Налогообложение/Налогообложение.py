g = lambda: [*map(int, input().split())]
from itertools import pairwise

X, k = g()
money = 0
for (a, b), p in zip(pairwise([0] + g() + [X]), g()):
    money += (min(b, X) - a) * p
    if X <= b:
        break
q, r = divmod(money, 100)
print(f"{q}.{r:02d}")