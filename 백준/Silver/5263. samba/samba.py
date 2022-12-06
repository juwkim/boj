g = lambda: [*map(int, input().split())]

from collections import defaultdict
n, k = g()
dic = defaultdict(int)
for _ in range(n):
    dic[input()] += 1
for key in dic:
    if dic[key] % k:
        print(key)
        break