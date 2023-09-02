g = lambda: [*map(int, input().split())]
while n:= int(input()):
    nums = g()
    ans = min(range(n), key=lambda i: abs(2023 - nums[i])) + 1
    print(ans)