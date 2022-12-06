for _ in range(int(input())):
    n = int(input())
    nums = [*map(int, input().split())]
    print(sum(len([1 for k in nums[:i] if k<= nums[i]]) for i in range(1, n)))