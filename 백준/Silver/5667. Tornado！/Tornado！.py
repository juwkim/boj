while True:
    try:
        N = int(input())
        nums = [*map(int, input().split())]
        ans = 0
        for i in range(N):
            if nums[i] == 0:
                zero = 1
                
                right = (i + 1) % N
                while nums[right] == 0:
                    zero += 1
                    nums[right] = 1
                    right = (right + 1) % N
        
                left = (i - 1) % N
                while nums[left] == 0:
                    zero += 1
                    nums[left] = 1
                    left = (left - 1) % N            
                
                ans += zero // 2        
        print(ans)
    except:
        break