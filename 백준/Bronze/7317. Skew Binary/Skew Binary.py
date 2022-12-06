for i in range(int(input())):
    n = int(input())
    res = n
    
    rank = 0
    while True:
        num = pow(2, rank + 1) - 1
        if num >= n:
            break
        rank += 1
    
    buf = []
    
    while n:
        if n >= num:
            buf.append(str(rank))
            n -= num
        else:
            rank -= 1
            num = pow(2, rank + 1) - 1
    
    print(res, '[' + ','.join(buf[::-1]) + ']')