g = lambda: [*map(int, input().split())]

from collections import Counter
input()
print(sum(v-1 for k, v in Counter(g()).items()))