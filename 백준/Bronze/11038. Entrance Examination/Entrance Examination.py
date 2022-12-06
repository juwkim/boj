while (s:= input()) != '0 0 0':
    m, nmin, nmax = map(int, s.split())
    nums = [int(input()) for _ in range(m)]
    print(max(range(nmin, nmax+1), key=lambda x: (nums[x-1] - nums[x], x)))