g = lambda: [*map(int, input().split())]

N, B = g()
nums = [int(input()) for _ in range(N)]
nums.sort(reverse=True)

i = 0
while B > 0:
    B -= nums[i]
    i += 1
print(i)