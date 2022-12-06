g = lambda: [*map(int, input().split())]

cnt = 1
while N:= int(input()):
    nums = [int(input()) for _ in range(N)]
    print('Machine', cnt)
    cnt += 1
    
    while (s:= input()) != '# 0':
        name, num = s.split()
        Sum = 0
        for _ in range(int(num)):
            a, time = g()
            Sum += nums[a-1] * time
        print(name, Sum)