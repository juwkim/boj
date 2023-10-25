import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

print("         NAME                     SOUNDEX CODE")
while True:
    try:
        name = input()
        code = [name[0]]
        for i in range(1, len(name)):
            p, c = name[i - 1], name[i]
            if c in 'BFPV':
                if p not in 'BFPV':
                    code.append('1')
            elif c in 'CGJKQSXZ':
                if p not in 'CGJKQSXZ':
                    code.append('2')
            elif c in 'DT':
                if p not in 'DT':
                    code.append('3')
            elif c == 'L':
                if p not in 'L':
                    code.append('4')
            elif c in 'MN':
                if p not in 'MN':
                    code.append('5')
            elif c == 'R':
                if p not in 'R':
                    code.append('6')
            if len(code) == 4:
                break
        code = ''.join(code) + '0' * (4 - len(code))
        print('         ', name, ' ' * (25 - len(name)), code, sep='')
    except:
        break
print("                   END OF OUTPUT")
