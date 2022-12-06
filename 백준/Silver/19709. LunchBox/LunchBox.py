g = lambda: [*map(int, input().split())]

N, M = g()
nums = sorted(int(input()) for _ in range(M))
ans = M
for i in range(M):
    N -= nums[i]
    if N < 0:
        ans = i
        break
print(ans)