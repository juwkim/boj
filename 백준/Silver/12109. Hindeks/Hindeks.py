g = lambda: [*map(int, input().split())]


N = int(input())
nums = sorted(g(), reverse=True)
ans = 0
for i in range(N):
    if nums[i] <= i:
        break
    ans = i + 1
print(ans)