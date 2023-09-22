import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

l, r = g()
ans = -1
for i in map(str, range(l, r + 1)):
    if len(set(i)) == len(i):
        ans = i
        break
print(ans)