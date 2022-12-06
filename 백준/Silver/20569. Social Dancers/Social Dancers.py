g = lambda: [*map(int, input().split())]

from collections import defaultdict
L, F, M = g()
lead, follow = defaultdict(int), defaultdict(int)
for _ in range(L):
    k, *dances = input().split()
    key = sorted(dance[0] for dance in dances)
    lead[''.join(key)] += 1
for _ in range(F):
    k, *dances = input().split()
    key = sorted(dance[0] for dance in dances)
    follow[''.join(key)] += 1

keys = "bcs bc cs bs b c s".split()
p = 0
for key in keys:
    num = min(lead[key], follow[key])
    lead[key] -= num
    follow[key] -= num
    p += num * len(key)

print(p * M / 3)