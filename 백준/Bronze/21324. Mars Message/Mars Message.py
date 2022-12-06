N = int(input())
nums = [float(input()) for _ in range(N)]
print(''.join([chr(int((nums[2*i] // 22.5)) * 16 + int(nums[2*i + 1] // 22.5)) for i in range(N // 2)]))