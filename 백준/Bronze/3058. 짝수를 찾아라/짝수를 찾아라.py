for _ in range(int(input())):
    nums = [*filter(lambda x: x % 2 == 0, map(int, input().split()))]
    print(sum(nums), min(nums))