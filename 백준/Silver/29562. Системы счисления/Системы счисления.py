def solve():
    n, b, c = map(int, input().split())
    idx, cnt = 0, 0
    nums = []
    while cnt < n:
        buf = []
        for d in range(1, c):
            if cnt + len(nums) >= n:
                return d * b ** idx + nums[n - cnt - 1]
            cnt += len(nums)
            buf.extend(d * b ** idx + num for num in nums)
        for d in range(c, b):
            if cnt + b ** idx >= n:
                return d * b ** idx + n - cnt - 1
            cnt += b ** idx
            buf.extend(d * b ** idx + num for num in range(b ** idx))
        idx += 1
        nums.extend(buf)
print(solve())