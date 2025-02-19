nums = [*map(int, input().split())]
t, idx = 0, 0
ans = [0, 0, 0]
T = int(input())
while t < T:
    d = min(nums[idx], T - t)
    t += d
    match idx:
        case 0:
            ans[2] += d
        case 1:
            ans[2] += d >> 1
        case 2:
            ans[1] += d
        case 3:
            ans[0] += d
        case 4:
            ans[0] += d
            ans[1] += d
    idx = (idx + 1) % 5
print(*ans)