from itertools import product

s = set(l.rstrip() for l in open(0))
for a, b in product("SBVK", map(str, range(1, 14))):
    t = f"{a} {b}"
    if t not in s:
        print(t)
        break