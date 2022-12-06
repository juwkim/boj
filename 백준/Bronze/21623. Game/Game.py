k, n = map(int, input().split())
rounds, score = 0, n

nums = [*map(int, input().split())]

for i in range(len(nums)):
    s = score - nums[i]
    if s == 0:
        rounds += 1
        if i == k - 1:
            score = 0
        else:
            score = n
    elif s > 0:
        score = s

print(rounds, score)
