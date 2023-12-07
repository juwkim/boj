import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
N, M, *l = map(int, open(0).read().split())
assert M == len(l)
ans = 'No'
g = N
for num in l:
    g = gcd(g, num)
    if g == 1:
        ans = 'Yes'
        break
print(ans)