import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
plus, sub, mul, div = g()

Min, Max = 1e9 + 1, -1e9 - 1
def solve(num, step, p, s, m, d):
    global Min, Max
    if step == N:
        Min = min(Min, num)
        Max = max(Max, num)
        return
    
    if p < plus:
        solve(num + nums[step], step + 1, p + 1, s, m, d)
    if s < sub:
        solve(num - nums[step], step + 1, p, s + 1, m, d)
    if m < mul:
        solve(num * nums[step], step + 1, p, s, m + 1, d)
    if d < div:
        if num >= 0:
            num //= nums[step]
        else:
            num = -((-num) // nums[step])
        solve(num, step + 1, p, s, m, d + 1)
    
solve(nums[0], 1, 0, 0, 0, 0)
print(Max)
print(Min)