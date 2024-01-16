import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
table = [g(), g()]
ans = 0
def solve(day, idx, cnt):
    global ans
    if day == N:
        ans += cnt >= M
        return
    for i in range(2):
        for j in range(3):
            if j == idx:
                solve(day + 1, j, cnt + table[i][j] // 2)
            else:
                solve(day + 1, j, cnt + table[i][j])
solve(0, -1, 0)
print(ans)