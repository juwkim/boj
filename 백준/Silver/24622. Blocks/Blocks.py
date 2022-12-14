from itertools import product, permutations, combinations
N = int(input())
buf = [input() for _ in range(4)]
check = set()
for i in range(1, 5):
    for l in combinations(buf, i):
        for a in product(*l):
            for b in permutations(a, i):
                check.add("".join(b))
for _ in range(N):
    if input() in check:
        print('YES')
    else:
        print('NO')