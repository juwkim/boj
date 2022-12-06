nums = [*map(int, input().split())]
def g(a, b):
    if nums[a] > nums[b]:
        nums[a], nums[b] = nums[b], nums[a]
        print(*nums)
while True:
    g(0, 1)
    g(1, 2)
    g(2, 3)
    g(3, 4)
    if nums == [1, 2, 3, 4, 5]:
        break