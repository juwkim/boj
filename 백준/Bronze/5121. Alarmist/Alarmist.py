g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n, w = g()
    nums = g()
    s = [sum(nums[i:i+w]) // w for i in range(n-w+1)]
    print(f'Data Set {cnt}:\n{max(s) - min(s)}\n')