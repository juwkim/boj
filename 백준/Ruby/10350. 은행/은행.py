import sys
input = lambda: sys.stdin.readline().rstrip('\n')

n = int(input())
nums = [*map(int, input().split())]
Sum = sum(nums)
cnt = 0
for i in range(n):
    tmp = 0
    for j in range(i, i+n):
        tmp += nums[j%n]
        if tmp < 0:
            r, q = divmod(-tmp, Sum)
            cnt += r + (q != 0)
print(cnt)