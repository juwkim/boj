import sys
input = sys.stdin.readline
from collections import defaultdict, Counter

X, Y = defaultdict(list), Counter()
for _ in range(int(input())):
    x, y = map(int, input().split())
    X[x].append(y)
    Y[y] += 1
ans = 0
for x in X:
    ans += (len(X[x]) - 1) * sum(Y[y] - 1 for y in X[x])
print(ans)