from itertools import combinations

K = int(input())
key = [*map(int, input())]
X = int(input())
Z = int(input())
results = set()
for comb in combinations(range(K), X):
    if sum(key[i] for i in comb) == Z:
        s = ['0'] * K
        for i in comb:
            s[i] = '1'
        results.add(''.join(s))
print(*results)