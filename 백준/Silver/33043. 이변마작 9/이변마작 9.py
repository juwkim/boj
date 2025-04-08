from collections import defaultdict, deque

N = int(input())
dic = defaultdict(lambda: deque(maxlen=5))
ans = 1e9
for i, c in enumerate(input().split()):
    dic[c].append(i)
    if len(dic[c]) == 5:
        ans = min(ans, i - dic[c][0] + 1)
print((ans, -1)[ans == 1e9])