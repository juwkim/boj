import sys
input = sys.stdin.readline
d = lambda p, q: (nums[p][0] - nums[q][0])**2 + (nums[p][1] - nums[q][1])**2

n = int(input())
nums = [[*map(int, input().split())] for _ in range(n)]
ans = 1e9
for i in range(n):
    visited = bytearray(n)
    def solve(v):
        visited[v] = 1
        u = -1
        for i in range(n):
            if visited[i] == False and (u == -1 or d(v, u) > d(v, i)):
                u = i
        if u == -1:
            return 0
        return solve(u) + d(v, u)
    ans = min(ans, solve(i))
print(ans)