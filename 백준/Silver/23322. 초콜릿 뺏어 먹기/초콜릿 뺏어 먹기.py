N, K, *a = map(int, open(0).read().split())
min, *nums = sorted(a)
cnt, day = 0, 0
for num in nums:
    if num > min:
        cnt += num - min
        day += 1
print(cnt, day)