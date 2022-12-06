N = int(input())
if N == 0:
    print('NO')
else:
    facto = 1
    num = 2
    while True:
        tmp = facto * num
        if tmp > N:
            break
        facto = tmp
        num += 1
    
    for i in range(num-1, 0, -1):
        if N >= facto:
            N -= facto
        if N == 0:
            break
        facto //= i
    
    print('YES' if N < 2 else 'NO')