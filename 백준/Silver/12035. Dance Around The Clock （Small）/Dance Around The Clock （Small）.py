import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

for _ in range(1, 1 + int(input())):
    D, K, N = g()
    nums = [*range(1, 1 + D)]
    for i in range(1, 1 + N):
        s = [-1, 1][i&1]
        for j in range(0, D, 2):
            nums[j], nums[j+s] = nums[j+s], nums[j]
    idx = nums.index(K)
    print(f'Case #{_}:', nums[(idx+1)%D], nums[idx-1])