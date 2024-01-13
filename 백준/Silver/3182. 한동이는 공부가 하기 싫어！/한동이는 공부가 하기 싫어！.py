import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = [int(input()) - 1 for _ in range(N)]
check = []
for i in range(N):
    visited = [False] * N
    cnt, cur = 0, i
    while not visited[cur]:
        visited[cur] = True
        cnt += 1
        cur = nums[cur]
    check.append(cnt)
ans = max(range(N), key=lambda x: check[x])
print(ans + 1)