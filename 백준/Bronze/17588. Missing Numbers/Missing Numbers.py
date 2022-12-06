n = int(input())
nums = [int(input()) for i in range(n)]
count = 0
for i in range(1, nums[-1]):
    if i not in nums:
        print(i)
        count += 1
if not count:
    print('good job')