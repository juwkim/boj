n = int(input())
nums = sorted(map(int, input().split()), reverse=True)

k = 0
while True:
    if all(num >= k for num in nums[:k]) and all(num <= k for num in nums[k:]):
        print(k)
        break
    k += 1