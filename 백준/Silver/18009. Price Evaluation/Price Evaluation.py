def g(): return [*map(int, input().split())]

for t in range(1, 1 + int(input())):

    n, m = g()
    dic = {}
    for _ in range(n):
        p, c = input().split()
        dic[p] = int(c)
    
    Min, Max = 0, 0
    check = set(dic)
    question = 0
    for p in input().split():

        if p == '?':
            question += 1
        else:
            Min += dic[p]
            Max += dic[p]
            check.remove(p)
    
    val_list = sorted([val for key, val in dic.items() if key in check])
    Min += sum(val_list[:question])
    Max += sum(val_list[len(val_list) - question:])

    print(f'Data Set {t}:')
    print(Min, Max)
    print()