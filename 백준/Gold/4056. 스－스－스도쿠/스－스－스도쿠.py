def solve(cnt):
    if cnt == 81:
        return 1
    r, q = divmod(cnt, 9)
    if Map[r][q]:
        return solve(cnt + 1)
    else:
        check = set()
        for i in range(9):
            check.add(Map[i][q])
        for j in range(9):
            check.add(Map[r][j])
        x = r - r % 3
        y = q - q % 3
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                check.add(Map[i][j])
        for i in range(1, 10):
            if i not in check:
                Map[r][q] = i
                if solve(cnt + 1):
                    return 1
        Map[r][q] = 0
    return 0

from collections import Counter
for _ in range(int(input())):
    Map = [[int(i) for i in input()] for _ in range(9)]
    buf = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            buf.append(Map[i][j:j+3] + Map[i+1][j:j+3] + Map[i+2][j:j+3])
    buf.extend(Map)
    buf.extend(zip(*Map))
    if any(any(line[i] > 1 for i in range(1, 10)) for line in map(Counter, buf)):
        print('Could not complete this grid.')
    elif solve(0):
        for line in Map:
            print(*line, sep='')
    else:
        print('Could not complete this grid.')
    print()