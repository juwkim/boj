Map = [[*input()] for _ in range(10)]

def check():
    if any('XXXXX' in ''.join(line) for line in Map):
        return 1
    if any('XXXXX' in ''.join(line) for line in zip(*Map)):
        return 1
    for i in range(6):
        a, b, c, d, e = Map[i:i+5]
        for l in zip(a, b[1:], c[2:], d[3:], e[4:]):
            if ''.join(l) == 'XXXXX':
                return 1
        for l in zip(a[4:], b[3:], c[2:], d[1:], e):
            if ''.join(l) == 'XXXXX':
                return 1
def solve():
    for i in range(10):
        for j in range(10):
            if Map[i][j] == '.':
                Map[i][j] = 'X'
                if check():
                    return 1                
                Map[i][j] = '.'
    return 0
print(solve())