g = lambda: [*map(int, input().split())]


N = int(input())
nums = sorted(g(), reverse=True)
total = sum(nums)
ans_A, ans_B = 0, 0

now = 0
for i in range(N):
    now += nums[i]
    A = (i + 1) / N
    B = now / total
    if B - A > ans_B - ans_A:
        ans_B = B
        ans_A = A
print(ans_A * 100, ans_B * 100)