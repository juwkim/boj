for _ in range(int(input())):
    nums = []
    while n := int(input()):
        nums.append(n)
    nums.sort(reverse=True)
    
    cost = 0
    for idx, num in enumerate(nums, 1):
        cost += pow(num, idx)
    cost <<= 1
    if cost > 5 * pow(10, 6):
        cost = 'Too expensive'
    print(cost)