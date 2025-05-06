import sys
input = sys.stdin.readline
from collections import OrderedDict

N, M = map(int, input().split())
cache = OrderedDict()
for _ in range(N):
    ID = int(input())
    if ID in cache:
        cache.move_to_end(ID, last=False)
    else:
        if len(cache) == M:
            cache.popitem()
        cache[ID] = True
        cache.move_to_end(ID, last=False)
print(*cache)