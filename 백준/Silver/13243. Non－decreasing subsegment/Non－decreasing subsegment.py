g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
start, end, prev, cur = 0, 0, 0, 0
while cur < N - 1:
    if nums[cur] > nums[cur + 1]:
        if cur - prev > end - start:
            end = cur
            start = prev
        prev = cur + 1
    cur += 1
if cur - prev > end - start:
    end = cur
    start = prev
print(end - start + 1, sum(nums[start:end + 1]))