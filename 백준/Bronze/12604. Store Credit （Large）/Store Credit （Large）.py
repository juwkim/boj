for i in range(1, 1+int(input())):
    C, P = map(int, [input(), input()])
    nums = [*map(int, input().split())]
    for j in range(P-1):
        for k in range(j+1, P):
            if nums[j] + nums[k] == C:
                print(f'Case #{i}: {j+1} {k+1}')
                break