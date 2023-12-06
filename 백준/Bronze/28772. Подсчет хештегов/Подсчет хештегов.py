import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

dic = defaultdict(int)
for word in input().split():
    if word.startswith("#") and len(word) >= 2 and all(c != "#" for c in word[1:]):
        dic[word] += 1
print(len(dic))
for k, v in sorted(dic.items(), key=lambda x: x[0]):
    print(k, v)