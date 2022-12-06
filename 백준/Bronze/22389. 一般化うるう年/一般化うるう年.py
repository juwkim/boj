while (s:= input()) != '0 0 0':
    n, l, r = map(int, s.split())
    nums = [int(input()) for _ in range(n)]
    cnt = 0
    for year in range(l, r+1):
        flag = True
        for i in range(n):
            if year % nums[i] == 0:
                cnt += 1 - (i & 1)
                flag = False
                break
        if flag:
            cnt += 1 - n & 1
    print(cnt)