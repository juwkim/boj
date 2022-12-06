for _ in range(int(input())):
    N = int(input())
    nums = [*map(int, input().split())]    
    if N & 1:
        s = 0
        while nums[N//2 + s] + nums[N//2 - s] == 2:
            s += 1
        print(N - 1 + 2 * s)
    else:
        l, r = N//2 - 1, N//2
        while nums[l] + nums[r] == 2:
            l -= 1
            r += 1
        print(2 * r)