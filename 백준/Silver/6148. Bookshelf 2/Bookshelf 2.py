import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]

N, B = g()
nums = [int(input()) for _ in range(N)]

ans = 1e10
def solve(num, idx):
    global ans
    if idx >= N:
        if num >= B:
            ans = min(ans, num - B)
        return
    solve(num, idx+1)
    solve(num + nums[idx], idx+1)

solve(0, 0)
print(ans)