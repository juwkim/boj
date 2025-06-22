import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, Counter
sys.setrecursionlimit(10**5)

n = int(input())
root = input()
tree = defaultdict(list)
for _ in range(n - 1):
    parent, child = input().split(' - ')
    tree[parent].append(child)

levels = Counter()
def solve(node, level):
    levels[level] += 1
    for child in tree[node]:
        solve(child, level + 1)
solve(root, 0)
print(max(levels.values()))