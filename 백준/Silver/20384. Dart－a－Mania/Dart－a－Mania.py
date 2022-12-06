nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 45, 48, 50, 51, 54, 57, 60]
check = set(nums)
while (N:= int(input())) > 0:
    com, per = 0, 0
    for i in range(43):
        for j in range(i, 43):
            a, b = nums[i], nums[j]
            target = N - a - b
            if target in check:
                if target == b:
                    com += 1
                    if a == b:
                        per += 1
                    else:
                        per += 3
                elif target > b:
                    com += 1
                    if a == b:
                        per += 3
                    else:
                        per += 6
    if com:
        print(f'NUMBER OF COMBINATIONS THAT SCORES {N} IS {com}.')
        print(f'NUMBER OF PERMUTATIONS THAT SCORES {N} IS {per}.')
    else:
        print(f'THE SCORE OF {N} CANNOT BE MADE WITH THREE DARTS.')
    print('**********************************************************************')
    pass
print('END OF OUTPUT')