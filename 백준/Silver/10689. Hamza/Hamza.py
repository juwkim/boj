g = lambda: [*map(int, input().split())]
for _ in range(1, 1 + int(input())):
    n = int(input())
    nums = g()
    Set = set(nums)

    for i in range(n):
        if nums[i] in Set:
            Set.remove(nums[i])
        if not Set:
            ans = i + 1
            break
    print(f'Case {_}:', ans)