import sys
from collections import Counter
lst = sorted(Counter(sys.stdin.readlines()).items())
cnt = sum(tree[1] for tree in lst)
for name, num in lst:
    print(name[:-1], f'{num * 100 / cnt:#.4f}')