g = lambda: [*map(int, input().split())]

from collections import Counter
n = int(input())
c = g()
k = int(input())
p = Counter(g())
for i in range(n):
    print('yes' if p[i+1] > c[i] else 'no')