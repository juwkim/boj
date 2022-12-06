while (s:=input()) != '0 0 0':
    N, M, P = map(int, s.split())
    nums = [int(input()) for _ in range(N)]
    if nums[M - 1]:
        print(sum(nums) * (100 - P) // nums[M - 1]) 
    else:
        print(0)