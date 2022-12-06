g = lambda: map(int, input().split())
for i in range(int(input())):
    c, n = g()
    nums = [*g()]
    for j in g():
        nums[j-1] -= 1
    print(f'Data Set {i+1}:\n{max(nums)}\n')