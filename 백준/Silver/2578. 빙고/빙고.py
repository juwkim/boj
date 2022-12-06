from sys import exit
import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]

row, col = {i: 0 for i in range(5)}, {i: 0 for i in range(5)}
diagonal = [0, 0]

Map = {}

for i_idx in range(5):
    for j_idx, num in enumerate(g()):
        row[i_idx] += num
        col[j_idx] += num
        Map[num] = (i_idx, j_idx)
        if i_idx == j_idx:
            diagonal[0] += num
        if i_idx + j_idx == 4:
            diagonal[1] += num

ans = 0
bingo = 0
for _ in range(5):
    for num in g():
        i_idx, j_idx = Map[num]
        
        row[i_idx] -= num
        col[j_idx] -= num
        
        bingo += row[i_idx] == 0
        bingo += col[j_idx] == 0  
        
        if i_idx == j_idx:
            diagonal[0] -= num
            bingo += diagonal[0] == 0
        if i_idx + j_idx == 4:
            diagonal[1] -= num
            bingo += diagonal[1] == 0
        
        
        ans += 1
        if bingo >= 3:
            print(ans)
            exit(0)