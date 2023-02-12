cnt = 1
while (s:= input()) != '0':
    n, *nums = map(int, s.split())
    if n & 1:
        ans = nums[n // 2]
    else:
        ans = (nums[n // 2] + nums[n // 2 - 1]) / 2
    print(f'Case {cnt}: {ans:.1f}')
    cnt += 1