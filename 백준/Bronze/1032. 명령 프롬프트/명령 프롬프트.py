N = int(input())
lines = []
for i in range(N):
    line = input()
    lines.append(line)
for j in range(len(lines[0])):
    s = set()
    for i in range(N):
        s.add(lines[i][j])
    if len(s) == 1:
        print(s.pop(), end='')
    else:
        print('?', end='')