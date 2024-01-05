import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
Out = [[] for _ in range(N + 1)]
In = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = g()
    Out[A].append(B)
    In[B] += 1

ans = []
solved = [False] * (N + 1)
solved_cnt = 0
while solved_cnt != N:
    for i in range(1, N + 1):
        if solved[i] or In[i]:
            continue
        solved[i] = True
        solved_cnt += 1
        ans.append(i)
        for j in Out[i]:
            In[j] -= 1
        break
print(*ans)