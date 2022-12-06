for cnt in range(1, 1 + int(input())):
    print(f'Case {cnt}:')
    Map = [[*input()] for _ in range(3)]
    me = input()
    
    flag = False
    good = [[me, me, '-'], [me, '-', me], ['-', me, me]]
    for i in range(3):
        if Map[i] in good:
            Map[i] = me * 3
            flag = True
            break
    if not flag:
        for j in range(3):
            tmp = [Map[0][j], Map[1][j], Map[2][j]]
            if tmp in good:
                Map[0][j] = me
                Map[1][j] = me
                Map[2][j] = me
                flag = True
                break
    if not flag:
        if [Map[0][0], Map[1][1], Map[2][2]] in good:
            Map[0][0] = me
            Map[1][1] = me
            Map[2][2] = me
        else:
            Map[0][2] = me
            Map[1][1] = me
            Map[2][0] = me
    for line in Map:
        print(*line, sep='')   