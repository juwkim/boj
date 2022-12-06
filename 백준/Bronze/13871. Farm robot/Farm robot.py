N, C, S = map(int, input().split())
nums = map(int, input().split())
now = 1
count = int(now == S)
for num in nums:
    now = (now + num - 1) % N + 1
    if now == S:
        count += 1
print(count)