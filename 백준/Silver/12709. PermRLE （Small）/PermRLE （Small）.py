from itertools import permutations, chain
for i in range(1, 1+int(input())):
    k, s = int(input()), input()
    a = zip(*map(lambda x: permutations(x, k), [s[i:i+k] for i in range(0, len(s), k)]))
    min_size = 99999999
    for line in a:
        p = [*chain(*line)]
        size = sum(m != n for m,n in zip(p, p[1:])) + 1
        min_size = min(min_size, size)
    print(f'Case #{i}: {min_size}')