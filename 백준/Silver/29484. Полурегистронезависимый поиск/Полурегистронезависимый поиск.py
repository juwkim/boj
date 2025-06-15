from collections import defaultdict

n = int(input())
groups = defaultdict(set)
for _ in range(n):
    name = input()
    groups[name.lower()].add(name)
for _ in range(int(input())):
    q = input()
    s = groups[q.lower()]
    print('-+'[len(s) == 1 or len(s) > 1 and q in s], end='')