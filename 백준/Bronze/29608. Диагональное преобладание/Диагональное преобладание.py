ans, cnt = "YES", 0
for i in range(int(input())):
    nums = [*map(int, input().split())]
    s = sum(nums)
    if s > 2 * nums[i]:
        ans = "NO"
        break
    cnt += 2 * nums[i] > s
if cnt == 0:
    ans = "NO"
print(ans)
if ans == "YES":
    print(cnt)