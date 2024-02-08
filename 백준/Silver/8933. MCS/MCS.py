import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import Counter, defaultdict

for _ in range(int(input())):
    k, W = input().split()
    k = int(k)
    cnt = Counter(W[:k])
    dic = defaultdict(int)
    dic[tuple(sorted((k, v) for k, v in cnt.items() if v))] += 1
    for i in range(k, len(W)):
        cnt[W[i]] += 1
        cnt[W[i-k]] -= 1
        dic[tuple(sorted((k, v) for k, v in cnt.items() if v))] += 1
    print(max(dic.values()))