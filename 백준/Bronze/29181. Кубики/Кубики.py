g = lambda: [*map(int, input().split())]

N = int(input())
nums = g()
q, r = divmod(sum(nums), N)

if r > N // 2:
    q += 1

l, h = 0, 0
for num in nums:
    if num == q:
        continue
    if num > q:
        h += num - q
    else:
        l += q - num
print(max(l, h))