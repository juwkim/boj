g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    cnt = 0
    N = int(input())
    nums = g()
    for i in range(N):
        if nums[i] == 0:
            cnt += 1
        while nums[i]:
            temp = i
            i = nums[i] - 1
            nums[temp] = 0           
    print(N - cnt)