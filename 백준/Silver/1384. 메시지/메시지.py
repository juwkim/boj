cnt = 1
while n := int(input()):
    print('Group', cnt)
    res = [input().split() for _ in range(n)]
    flag = True
    for i in range(n):
        for j in range(1, n):
            if res[i][j] == 'N':
                flag = False
                print(res[i-j][0], 'was nasty about', res[i][0])
    if flag:
        print('Nobody was nasty')
    
    cnt += 1
    print()