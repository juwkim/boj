import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

K, N = g()
dic = defaultdict(list)
for _ in range(K):
    word = input()
    dic[word[0]].append(word)
for key in dic:
    dic[key].sort()
idx = {key: 0 for key in dic}
for _ in range(N):
    c = input()
    word = dic[c][idx[c]]
    idx[c] = (idx[c] + 1) % len(dic[c])
    print(word)