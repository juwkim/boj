for _ in range(int(input())):
    J, N = map(int, input().split())
    nums = sorted([eval(input().replace(' ', '*')) for _ in range(N)], reverse=True)
    t, i = 0, 0
    while t < J:
        t += nums[i]
        i += 1
    print(i)