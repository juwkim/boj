import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import deque
def bfs():
    qu = deque([1])

    ret = 0
    while True:
        ret += 1
        Next_qu = deque()
        for x in qu:
            for Next in map(jump.get, range(x+1, min(x+7, 101))):
                if Next == 100:
                    return ret
                if visited[Next] == 0:
                    visited[Next] = 1
                    Next_qu.append(Next)
        qu = Next_qu


jump = {i: i for i in range(1, 101)}
for _ in range(sum(g())):
    x, y = g()
    jump[x] = y

visited = [0 for _ in range(101)]
print(bfs())