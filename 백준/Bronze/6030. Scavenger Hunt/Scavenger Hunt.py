from itertools import product
P, Q = map(int, input().split())
ps = [i for i in range(1, P+1) if P%i == 0]
qs = [i for i in range(1, Q+1) if Q%i == 0]
for pair in product(ps, qs):
    print(*pair)