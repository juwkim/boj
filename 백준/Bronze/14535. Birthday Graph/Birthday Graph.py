i = 1
name = [' '  , 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

while n:=int(input()):
    month = [0]*13
    for _ in [0] * n:
        month[int(input().split()[1])] += 1
    print(f'Case #{i}:')
    for j in range(1, 13):
        print(f'{name[j]}:{"*"*month[j]}')
    i += 1