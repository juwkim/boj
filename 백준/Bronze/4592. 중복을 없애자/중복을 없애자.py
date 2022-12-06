while (n:= input()) != '0':
    nums = [0]
    for num in n.split()[1:]:
        if num != nums[-1]:
            nums.append(num)
    print(*nums[1:], '$')