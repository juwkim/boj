g = lambda: [*map(int, input().split())]

N, score, P = g()
if N:
    nums = g()
    cnt = 1
    for i in range(N):
        if nums[i] > score:
            cnt += 1
    a = nums.count(score)
    if cnt + a > P:
        print(-1)
    else:
        print(cnt)    
else:
    print(1)