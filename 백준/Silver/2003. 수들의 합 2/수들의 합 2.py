N, M = map(int, input().split())
nums = [*map(int, input().split())]
cnt, btm, top, prefix_sum = 0, 0, 1, 0
while top <= N:
    prefix_sum = sum(nums[btm:top])
    if prefix_sum == M:
        cnt += 1
        btm += 1
        top += 1
    elif prefix_sum > M:
        btm += 1
    else:
        top += 1
print(cnt)