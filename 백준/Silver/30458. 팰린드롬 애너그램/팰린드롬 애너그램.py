import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter

N = int(input())
S = input()
if N&1:
    cnt = Counter(S[:N//2] + S[N//2+1:])
else:
    cnt = Counter(S)
print('Yes' if all(v%2==0 for v in cnt.values()) else 'No')