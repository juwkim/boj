g = lambda: [*map(int, input().split(', '))]

for _ in range(int(input())):
    N = int(input())    
    nums = [[min(i, 100) for i in g()] for _ in range(N)]
    C = max(len(l) for l in nums)
    
    ans = -1
    for i in range(N):
        m = sum(nums[i]) / C
        v = sum((num - m) ** 2 for num in nums[i]) / C
        if v > ans:
            ans = v
            idx = i

    print(f'{idx + 1}\t{ans:.2f}')