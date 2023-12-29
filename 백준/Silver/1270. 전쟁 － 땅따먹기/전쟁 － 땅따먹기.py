import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter
for _ in range(int(input())):
    T, *nums = g()
    cnt = Counter(nums)
    k, v = cnt.most_common(1)[0]
    if 2 * v > int(T):
        print(k)
    else:
        print("SYJKGW")