import sys
input = lambda: sys.stdin.readline().rstrip()

while n:=int(input()):
    res = []
    for _ in range(n):
        s = input()
        depth, content = s.count('.'), s.lstrip('.')
        if depth:
            res.append(' ' * (depth - 1) + '+' + content)
        else:
            res.append(content)

    for i in range(len(res) - 1):
        d = res[i].find('+')
        if d == -1:
            continue
        j = i + 1
        while j < len(res) and len(res[j]) > d and res[j][d] == ' ':
            j += 1
        if j < len(res) and len(res[j]) > d and res[j][d] == '+':
            for k in range(i + 1, j):
                if d:
                    res[k] = res[k][:d] + '|' + res[k][d + 1:]
                else:
                    res[k] = '|' + res[k][1:]
    print(*res, sep='\n')