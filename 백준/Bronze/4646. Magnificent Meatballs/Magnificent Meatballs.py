while (s := input())[0] != '0':
    N, *table = map(int, s.split())
    a, b = 0, sum(table)
    flag = True
    for i in range(N-1):
        a += table[i]
        b -= table[i]
        if a == b:
            print(f'Sam stops at position {i+1} and Ella stops at position {i+2}.')
            flag = False
            break
    if flag:
        print('No equal partitioning.')