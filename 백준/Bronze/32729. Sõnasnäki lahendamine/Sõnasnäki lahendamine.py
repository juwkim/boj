import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

cnt = Counter(input())
for _ in range(int(input())):
    word = Counter(s:=input())
    if all(cnt[c] >= word[c] for c in word):
        print(s)