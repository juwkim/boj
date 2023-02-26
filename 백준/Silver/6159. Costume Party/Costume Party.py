g = lambda: [*map(int, input().split())]
I = lambda: int(input())

N, S = g()
nums = sorted(I() for _ in range(N))
cnt = 0
l, r = 0, N-1
while l != r:
    if nums[l] + nums[r] > S:
        r -= 1
    else:
        cnt += r - l
        l += 1
print(cnt)