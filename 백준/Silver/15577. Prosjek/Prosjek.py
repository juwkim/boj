N = int(input())
cur, *nums = sorted(int(input()) for _ in range(N))
for num in nums:
    cur = (cur + num) / 2
print(cur)