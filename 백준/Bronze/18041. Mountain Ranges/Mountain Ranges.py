N, X = map(int, input().split())
nums = [*map(int, input().split())]
count, max_count = 1, 1
for i in range(N-1):
    if nums[i+1] - nums[i] <= X:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 1
print(1 if N == 1 else 0 if max_count == 1 else max_count)