import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().split())
    q = deque()
    visit = [0] * 10000
    q.append((A, ''))
    visit[A] = 1
    while q:
        n, operation = q.popleft()
        if n == B:
            print(operation)
            break

        D_num = (2*n)%10000
        if visit[D_num] == 0:
            q.append((D_num, operation+'D'))
            visit[D_num] = 1
        
        S_num = n-1 if n!=0 else 9999
        if visit[S_num] == 0:
            q.append((S_num, operation+'S'))
            visit[S_num] = 1
        
        L_num = 10*(n%1000) + n//1000
        if visit[L_num] == 0:
            q.append((L_num, operation+'L'))
            visit[L_num] = 1
        
        R_num = 1000*(n%10) + n//10
        if visit[R_num] == 0:
            q.append((R_num, operation+'R'))
            visit[R_num] = 1