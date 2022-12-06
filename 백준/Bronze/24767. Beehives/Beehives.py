while True:
    s = input()
    if s == '0.0 0':
        break
    d, N = s.split()
    N = int(N)
    d = float(d)
    nums = [[*map(float, input().split())] for _ in range(N)]
    a, b = 0, 0
    res = [0] * N
    for i in range(N-1):
        for j in range(i+1, N):
            if (nums[i][0] - nums[j][0]) ** 2 + (nums[i][1] - nums[j][1]) ** 2 < d * d:
                res[i] = 1
                res[j] = 1
    a = sum(res)
    print(f'{a} sour, {N - a} sweet')