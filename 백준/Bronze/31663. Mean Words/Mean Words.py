import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import zip_longest

for l in zip_longest(*[input() for _ in range(int(input()))]):
    l = [c for c in l if c]
    print(chr(sum(map(ord, l)) // len(l)), end='')