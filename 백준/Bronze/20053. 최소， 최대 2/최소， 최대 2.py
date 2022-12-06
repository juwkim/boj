T = int(input())
for _ in range(T):
    N = int(input())
    nums = [*map(int, input().split())]
    print(min(nums), max(nums))