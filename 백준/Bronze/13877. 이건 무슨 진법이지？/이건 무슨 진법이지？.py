for i in range(1, 1+int(input())):
    num = input().split()[1]
    if '8' in num or '9' in num:
        eight = 0
    else:
        eight = int(num, 8)
    print(f'{i} {eight} {int(num)} {int(num, 16)}')