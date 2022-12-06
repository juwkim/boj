while (s:=input()) != '0':
    k, *nums = map(int, s.split())
    count = 0
    for i in range(k):
        print(f'{i+1} ' * (nums[i] - count), end='')
        count = nums[i]