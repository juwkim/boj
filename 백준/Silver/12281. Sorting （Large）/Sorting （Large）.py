import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]


for _ in range(1, 1 + int(input())):
    N = int(input())
    nums = g()
    Alex, Bob = [], []
    for i in range(N):
        if nums[i] & 1:
            Alex.append(nums[i])
            nums[i] = 1
        else:
            Bob.append(nums[i])
            nums[i] = 0
    Alex.sort(reverse=True)
    Bob.sort()
    
    print(f'Case #{_}:', end=' ')
    for num in nums:
        if num:
            print(Alex.pop(), end=' ')
        else:
            print(Bob.pop(), end=' ')
    print()