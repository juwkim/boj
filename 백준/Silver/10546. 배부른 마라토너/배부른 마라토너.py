import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import Counter
N = int(input())
cnt = Counter(input() for _ in range(N))
for _ in range(N-1):
    cnt[input()] -= 1
for name in cnt:
    if cnt[name] == 1:
        print(name)
        break