g = lambda: [*map(int, input().split())]

for cnt in range(1, 1 + int(input())):
    n = int(input())
    nums = [*map(float, input().split())]
    
    start = -1
    for i in range(n):
        if 30.0 <= nums[i] <= 30.2:
            start = i
            break
    if 0 <= start < n - 3:
        ans = min(nums[start+3:]) - 30
    else:
        ans = 0.00
    print(f'Data Set {cnt}:\n{ans:.2f}\n')