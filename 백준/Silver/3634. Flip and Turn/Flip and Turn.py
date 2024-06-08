m, n = map(int, input().split())
mat = [input() for _ in range(m)]
p = []
def add(s):
    for c in s:
        if not p or p[-1] != c: p.append(c)
        else: p.pop()
for c in input():
    match c:
        case '1': add('t')
        case '2': add('ftf')
        case 'H': add('f')
        case 'V': add('tft')
        case 'A' | 'Z': add('ft')
        case 'B' | 'Y': add('ftft')
        case 'C' | 'X': add('ftftft')

for c in p:
    if c == 't': mat = [*zip(*mat)]
    else: mat = mat[::-1]

print(len(mat), len(mat[0]))
for l in mat:
    print(*l, sep='')