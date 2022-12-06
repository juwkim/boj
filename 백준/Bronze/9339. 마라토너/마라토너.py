g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    K = int(input())
    nums = g()
    N = int(input())
    
    cnt, top_res, first = 0, 1000, 0
    for _ in range(N):
        num, h, m = g()
        res = h * 60 + m
        if num in nums and 0 < res <= 360:
            cnt += 1
            if res < top_res:
                top_res = res
                first = num
    print(first, cnt)