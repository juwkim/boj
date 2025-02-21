import sys
input = sys.stdin.readline
from collections import Counter

cnt = Counter()
for _ in range(int(input())):
    name, num = input().split()
    cnt[name] += int(num)
for name in sorted(cnt):
    print(name, cnt[name])