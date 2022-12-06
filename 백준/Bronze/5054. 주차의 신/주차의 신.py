for _ in range(int(input())):
    input()
    nums = [*map(int, input().split())]
    print(2*(max(nums) - min(nums)))