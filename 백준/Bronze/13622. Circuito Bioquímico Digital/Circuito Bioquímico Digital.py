g = lambda: [*map(int, input().split())]

while (s:= input()) != '0 0 0':
    P, N, C = map(int, s.split())
    nums = [g() for _ in range(N)]
    t_nums = [*map(list, zip(*nums))]
    ans = 0
    for line in t_nums:
        cnt = 0
        for num in line:
            if num == 1:
                cnt += 1
            else:
                ans += (cnt >= C)
                cnt = 0
        ans += (cnt >= C)
    print(ans)