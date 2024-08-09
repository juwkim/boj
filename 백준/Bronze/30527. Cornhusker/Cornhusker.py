nums = [*map(int, input().split())]
N, KWF = map(int, input().split())
print(sum(nums[i] * nums[i + 1] for i in range(0, 10, 2)) // 5 * N // KWF)