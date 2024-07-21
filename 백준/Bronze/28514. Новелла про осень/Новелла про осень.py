from itertools import pairwise

n = int(input())
k = input()
d = {*pairwise(k)}; d.add((k[-1], k[0]))
print(("NO", "YES")[all(x in d for x in pairwise(input()))])