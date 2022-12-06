import sys
input = lambda: sys.stdin.readline().rstrip('\n')


g = lambda: [*map(int, input().split())]


from collections import defaultdict
dic = defaultdict(int)
N, M = g()
Map = [input() for _ in range(N)]
for i in range(N-2):
    for j in range(M-2):
        tmp = Map[i][j] + Map[i+1][j+1] + Map[i+2][j+2]
        if tmp[0] == tmp[1] and tmp[1] != tmp[2] and tmp[0] != 'O' and tmp[2] != 'M':
            dic[tmp[::-1]] += 1
        elif tmp[2] == tmp[1] and tmp[1] != tmp[0] and tmp[0] != 'M' and tmp[2] != 'O':
            dic[tmp] += 1
    for j in range(2, M):
        tmp = Map[i][j] + Map[i+1][j-1] + Map[i+2][j-2]
        if tmp[0] == tmp[1] and tmp[1] != tmp[2] and tmp[0] != 'O' and tmp[2] != 'M':
            dic[tmp[::-1]] += 1
        elif tmp[2] == tmp[1] and tmp[1] != tmp[0] and tmp[0] != 'M' and tmp[2] != 'O':
            dic[tmp] += 1

Map += [''.join(l) for l in zip(*Map)]
for line in Map:
    for i in range(len(line)-2):
        tmp = line[i:i+3]
        if tmp[0] == tmp[1] and tmp[1] != tmp[2] and tmp[0] != 'O' and tmp[2] != 'M':
            dic[tmp[::-1]] += 1
        elif tmp[2] == tmp[1] and tmp[1] != tmp[0] and tmp[0] != 'M' and tmp[2] != 'O':
            dic[tmp] += 1

if dic:
    print(max(dic.values()))
else:
    print(0)