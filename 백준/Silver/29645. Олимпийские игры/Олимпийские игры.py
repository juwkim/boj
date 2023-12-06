import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

gold = defaultdict(int)
silver = defaultdict(int)
bronze = defaultdict(int)

for _ in range(int(input())):
    a, b, c = input().split()
    gold[a] += 1
    silver[b] += 1
    bronze[c] += 1

nations = gold.keys()
winner = min(nations, key=lambda x: (-gold[x], -silver[x], -bronze[x], x))
print(winner)