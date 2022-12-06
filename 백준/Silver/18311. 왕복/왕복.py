g = lambda: [*map(int, input().split())]

N, K = g()
nums = g()
ans = None
for i in range(N):
    K -= nums[i]
    if K < 0:
        ans = i + 1
        break
if ans == None:
    for i in range(N-1, -1, -1):
        K -= nums[i]
        if K < 0:
            ans = i + 1
            break
print(ans)