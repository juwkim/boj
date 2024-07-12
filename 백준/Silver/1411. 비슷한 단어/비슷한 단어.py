import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations
from collections import defaultdict

words = []
for _ in range(int(input())):
    d = defaultdict(list)
    for i, c in enumerate(input()):
        d[c].append(i)
    words.append(sorted(d.values()))
print(sum(a == b for a, b in combinations(words, 2)))