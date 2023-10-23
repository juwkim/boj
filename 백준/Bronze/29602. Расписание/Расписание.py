import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
ans = [-1] * N
day = 1
for idx, _ in sorted(enumerate(g()), key=lambda x: x[1]):
    ans[idx] = day
    day += 1
print(*ans)