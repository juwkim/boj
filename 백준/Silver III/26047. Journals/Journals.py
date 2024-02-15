from itertools import pairwise

cnt = 0
for a, b in pairwise(input()):
    cnt += a == b
print((cnt + 1) // 2)