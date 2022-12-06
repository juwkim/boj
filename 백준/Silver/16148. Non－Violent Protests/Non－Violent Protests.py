for _ in range(1, 1 + int(input())):
    n = int(input())
    nums = sorted(map(int, input().split()))
    for i in range(n):
        if nums[i] > i:
            n = i
            break
    print(f'Data Set {_}:\n{n}\n')