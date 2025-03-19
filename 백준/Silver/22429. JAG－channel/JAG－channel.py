import sys
input = lambda: sys.stdin.readline().rstrip()

while n:=int(input()):
    lines = [input() for _ in range(n)]
    result = []
    for i, line in enumerate(lines):
        depth = line.count('.')
        content = line.lstrip('.')
        
        if depth == 0:
            result.append(content)
        else:
            prefix = ' ' * (depth - 1) + '+'
            result.append(prefix + content)

    for i in range(len(result) - 1):
        curr_depth = result[i].find('+')
        if curr_depth == -1:
            continue
        j = i + 1
        while j < len(result) and len(result[j]) > curr_depth and result[j][curr_depth] == ' ':
            j += 1
        if j < len(result) and len(result[j]) > curr_depth and result[j][curr_depth] == '+':
            for k in range(i + 1, j):
                if curr_depth:
                    result[k] = result[k][:curr_depth] + '|' + result[k][curr_depth + 1:]
                else:
                    result[k] = '|' + result[k][1:]
    print(*result, sep='\n')