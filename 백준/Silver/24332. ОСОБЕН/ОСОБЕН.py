import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

s = input()
check = defaultdict(lambda: -1)
l = 0
ans = [0, 0]
for i, c in enumerate(s):
    if check[c] == -1:
        check[c] = i
    else:
        if i - l >= ans[0]:
            ans = [i - l, l]
        for j in range(l, check[c]):
            check[s[j]] = -1
        l = check[c] + 1
        check[c] = i
if len(s) - l >= ans[0]:
    ans = [len(s) - l, l]
print(*ans)
print(s[ans[1]:ans[1] + ans[0]])