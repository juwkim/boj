from collections import *
from itertools import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    l = [i[0] + '-' for i in input().split()]
    for key in product(*l):
        dic[''.join(key)] += 1
for _ in range(m):
    key = ''.join([i[0] for i in input().split()])
    print(dic[key])