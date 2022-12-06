a = '*.,!? *abc*def*ghi*jkl*mno*pqrs*tuv*wxyz'.split('*')
for _ in range(int(input())):
    for num in input().split('0'):
        if num:
            p = a[int(num[0])]
            print(p[(len(num) - 1) % len(p)], end='')      
    print()