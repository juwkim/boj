nums = [*map(int, input().split())]
a = [[i, nums[i]] for i in range(len(nums)) if nums[i] > 0]
d = (a[0][1] - a[1][1])/(a[0][0] - a[1][0])
if d != int(d):
    print(-1)
else:
    d = int(d)
    for j in range(-a[0][0], 10-a[0][0]):
        print(a[0][1] + d*j, end=' ')