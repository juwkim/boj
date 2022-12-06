Set = {'O', 'WO', 'WS', 'ES', 'MS', 'CS', 'IS', 'OS', 'SS'}
for _ in range(int(input())):
    Map = [input().split() for _ in range(9)]
    Map += [*zip(*Map)]
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = Map[i][j:j+3] + Map[i+1][j:j+3] + Map[i+2][j:j+3]
            Map.append(tmp)
    if all(set(line) == Set for line in Map):
        print('all 3')
    else:
        print('not')