import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

v, k = g()
ans = set()
for i in range(v, 0, -1):
    if i + k in ans:
        continue
    ans.add(i)
print(len(ans))
print(*sorted(ans, reverse=True), sep='\n')