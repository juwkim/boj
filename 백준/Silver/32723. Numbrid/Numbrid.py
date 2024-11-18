N = int(input())
nums = [*map(int, input().split())]
ans = sorted({*range(min(nums), max(nums))} - {*nums})
print(len(ans))
print(*ans)