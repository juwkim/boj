g = lambda: [*map(int, input().split())]

N, X = g()
nums = sorted(g())

ans = 1
for i in range(N-1):
    if nums[i] + nums[i+1] > X:
        break
    ans += 1
print(ans)