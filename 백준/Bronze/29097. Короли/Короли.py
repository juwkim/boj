n, m, k, a, b, c = map(int, input().split())
nums = n * a, m * b, k * c
l = max(nums)
ans = [name for num, name in zip(nums, ("Joffrey", "Robb", "Stannis")) if num == l]
print(*ans)