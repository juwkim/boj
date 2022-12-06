g = lambda: [*map(int, input().split())]
N = int(input())
energy, joy = g(), g()
ans = 0
def solve(idx, consume, num):
    global ans
    if idx == N:
        ans = max(ans, num)
        return
    
    if consume + energy[idx] < 100:
        solve(idx + 1, consume + energy[idx], num + joy[idx])
    solve(idx + 1, consume, num)

solve(0, 0, 0)
print(ans)