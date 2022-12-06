i = 1
while True:
    n = int(input())
    if n == 0:
        break
    nums = [list(map(int, input().split())) for _ in range(n)]
    total = nums[0][0]
    if n > 1:
        total += sum(nums[-1])
    if n > 2:
        total += sum(sum([i[0], i[-1]]) for i in nums[1:-1])
    print(f'Case #{i}:{total}')
    i += 1