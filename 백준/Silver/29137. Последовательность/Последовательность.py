import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
ans = [0, 0]
for num in g():
    ans.append(num - ans[-1] - ans[-2])
print(*ans)