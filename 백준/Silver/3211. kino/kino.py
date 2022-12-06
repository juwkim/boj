N = int(input())
nums = sorted(int(input()) for _ in range(N))
for i in range(N):
    if i >= nums[i]:
        print(i + 1)
        break