g = lambda: [*map(int, input().split())]

import sys
input = sys.stdin.readline

from collections import defaultdict
from itertools import product
n, m = g()
dic = defaultdict(int)
for _ in range(n):
    l = [i[0] + '-' for i in input().split()]
    for key in product(*l):
        dic[''.join(key)] += 1
for _ in range(m):
    key = ''.join([i[0] for i in input().split()])
    print(dic[key])