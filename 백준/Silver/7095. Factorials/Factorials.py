N = int(input())
buf = [0, 3, 1, 2]
res = [[], [1, 2, 3], [4], [5, 6]]
if N < 4:
    print(buf[N])
    for num in res[N]:
        print(num)
else:
    x = 2
    num = 1
    
    cnt = 1
    while True:
        num *= x
        while num >= 10:
            num /= 10
            cnt += 1
        if cnt == N:
            print(1, x)
            break
        if cnt > N:
            print('NO')
            break
        x += 1