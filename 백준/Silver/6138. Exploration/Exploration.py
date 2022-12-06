T, N = map(int, input().split())
nums = [0] + sorted([int(input()) for _ in range(N)], key=abs)
for i in range(1, 1 + N):
    T -= abs(nums[i] - nums[i-1])
    if T < 0:
        break
print(i-1)