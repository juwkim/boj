import sys
input = sys.stdin.readline

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
a = sorted(range(N), key=lambda x: nums[x], reverse=True)
b = sorted(range(N), key=lambda x: (nums[x][1], nums[x][0]), reverse=True)
ans, l, r = 0, 0, 0
for i in range(N):
    if i & 1:
        while l < N and nums[a[l]][0] == -1:
            l += 1
        while r < N and nums[b[r]][0] == -1:
            r += 1
        if nums[a[l]][0] - nums[a[l]][1] > nums[b[r]][1] - nums[b[r]][1]:
            ans -= nums[a[l]][1]
            nums[a[l]] = (-1, -1)
            l += 1
        else:
            ans -= nums[b[r]][1]
            nums[b[r]] = (-1, -1)
            r += 1
    else:
        while l < N and nums[a[l]][0] == -1:
            l += 1
        while r < N and nums[b[r]][0] == -1:
            r += 1
        if nums[a[l]][0] - nums[a[l]][1] < nums[b[r]][1] - nums[b[r]][1]:
            ans += nums[b[r]][0]
            nums[b[r]] = (-1, -1)
            r += 1
        else:
            ans += nums[a[l]][0]
            nums[a[l]] = (-1, -1)
            l += 1
print(ans)