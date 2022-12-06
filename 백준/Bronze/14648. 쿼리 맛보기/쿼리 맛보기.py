n, q = map(int, input().split())
nums = [*map(int, input().split())]
for i in range(q):
    c, *l = map(int, input().split())
    if c == 1:
        a, b = l
        print(sum(nums[a-1:b]))
        nums[a-1], nums[b-1] = nums[b-1], nums[a-1]
    else:
        a, b, c, d = l
        print(sum(nums[a-1:b]) - sum(nums[c-1:d]))