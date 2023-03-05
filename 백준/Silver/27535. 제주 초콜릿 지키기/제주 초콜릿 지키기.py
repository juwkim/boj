g = lambda: [*map(int, input().split())]

cnt = g()
base = sum(cnt) % 10
if base == 0 or base == 1:
    base = 10

for _ in range(int(input())):
    for idx, num in enumerate(g()):
        cnt[idx] -= num
    Sum = sum(cnt)
    
    num = Sum
    base_num = ''
    while True:
        num, r = divmod(num, base)
        base_num = str(r) + base_num
        if num == 0:
            break
    
    print(base_num, '7H', sep='')
    if base_num == '0':
        print('NULL')
    else:
        ans = sorted([(0, 'H'), (1, 'T'), (2, 'C'), (3, 'K'), (4, 'G')], key=lambda x: (-cnt[x[0]], x[1]))
        for idx, alpha in ans:
            if cnt[idx] == 0:
                break
            print(alpha, end='')
        print()
    
    base = Sum % 10
    if base == 0 or base == 1:
        base = 10