import sys
input = sys.stdin.readline

def dfs(i):
    if not buf[i]:
        if visited[i]:
            return 1
        visited[i] = 1
        return 0
    for ni in buf[i]:
        if dfs(ni):
            return 1
    return 0

for tc in range(1, 1 + int(input())):
    N = int(input())
    buf = [[]]
    for _ in range(N):
        M, *nums = map(int, input().split())
        buf.append(nums)
    ans = "No"
    for i in range(1, N + 1):
        visited = bytearray(N + 1)
        if dfs(i):
            ans = "Yes"
            break
    print(f"Case #{tc}: {ans}")