n, k, p = map(int, input().split())
nums = (n - k + 1) * 100 + (n + 4) * p, (2 * n - k + 6) * 100 - (n + 4) * p, (n + 4) * 100
print(("continue", "backspace", "restart")[min(range(3), key=lambda x: nums[x])])