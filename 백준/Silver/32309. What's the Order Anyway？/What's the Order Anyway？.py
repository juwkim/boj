import sys
input = sys.stdin.readline
from itertools import permutations

n, c = map(int, input().split())
rule = []
alpha = set()
for _ in range(c):
    a, x, y = input().split()
    alpha.add(x)
    alpha.add(y)
    rule.append((a, x, y))
c = ord('A')
while len(alpha) != n:
    alpha.add(chr(c))
    c += 1
ans = 0
for s in map(''.join, permutations(alpha, n)):
    for a, x, y in rule:
        if a == '1':
            if s.index(x) < s.index(y):
                break
        elif a == '2':
            if s.index(x) > s.index(y):
                break
        else:
            if x + y in s or y + x in s:
                break
    else:
        ans += 1
print(ans)