g = lambda: [*map(int, input().split())]

while (s:= g())[0]:
    N, A, B, C, X = s
    nums = g()
    cnt = 0
    idx = 0
    if X == nums[idx]:
        idx += 1
    
    while idx < N and cnt < 10000:
        cnt += 1
        X = (A * X + B) % C
        if X == nums[idx]:
            idx += 1
    if idx == N and cnt <= 10000:
        print(cnt)
    else:
        print(-1)