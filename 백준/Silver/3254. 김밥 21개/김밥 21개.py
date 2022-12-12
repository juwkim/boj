def check():
    flag = False
    for line in Map:
        s = ''.join(line)
        if '1111' in s:
            return 'sk'
        if '2222' in s:
            flag = True

    for line in zip(*Map):
        s = ''.join(line)
        if '1111' in s:
            return 'sk'
        if '2222' in s:
            flag = True
    
    for i in range(3):
        s = [''.join(l) for l in zip(Map[i], Map[i+1][1:], Map[i+2][2:], Map[i+3][3:])]
        t = [''.join(l) for l in zip(Map[i][3:], Map[i+1][2:], Map[i+2][1:], Map[i+3])]
        if '1111' in s or '1111' in t:
            return 'sk'
        if '2222' in s or '2222' in t:
            flag = True
    if flag:
        return 'ji'
    return 0

Map = [['0'] * 7 for _ in range(6)]
for step in range(1, 22):
    si, ji = map(lambda x: int(x) - 1, input().split())

    for i in range(5, -1, -1):
        if Map[i][si] == '0':
            Map[i][si] = '1'
            break
    for i in range(5, -1, -1):
        if Map[i][ji] == '0':
            Map[i][ji] = '2'
            break
    
    win = check()
    if win:
        print(win, step)
        break
if win == 0:
    print('ss')