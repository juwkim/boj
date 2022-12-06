s = 0.00000001
n = int(input())
if n:
    k = round(n * 0.15 + s)
    nums = sorted(int(input()) for _ in range(n))[k:n-k]
    ans = sum(nums) / len(nums)
    print(round(ans + s))
else:
    print(0)