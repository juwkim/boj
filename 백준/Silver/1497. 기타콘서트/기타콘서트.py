N, M = map(int, input().split())
nums = []
for _ in range(N):
    _, yn = input().split()
    num = 0
    for i in range(M):
        if yn[i] == 'Y':
            num |= 1 << i
    if num:
        nums.append(num)

ans = 0, 0
def solve(idx, num, cnt):
    global ans
    if idx == len(nums):
        if num.bit_count() > ans[0].bit_count() or (num.bit_count() == ans[0].bit_count() and cnt < ans[1]):
            ans = num, cnt
        return
    solve(idx + 1, num | nums[idx], cnt + 1)
    solve(idx + 1, num, cnt)
solve(0, 0, 0)
if ans == (0, 0):
    print(-1)
else:
    print(ans[1])