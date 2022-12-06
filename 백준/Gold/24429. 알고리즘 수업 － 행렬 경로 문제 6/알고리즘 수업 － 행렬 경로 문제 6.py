import sys
input = sys.stdin.readline

g = lambda: map(int, input().split())
N = int(input())
nums = [tuple(g()) for _ in range(N)]

check = {}
flag = False
for _ in range(int(input())):
    i, j = g()
    if check.get(i+j):
        flag = True
        break
    check[i+j] = i, j
if flag:
    print(-1)
else:
    l = sorted(check.keys())
    if all(check[l[i]][0] <= check[l[i+1]][0] and check[l[i]][1] <= check[l[i+1]][1] for i in range(len(l)-1)):
        d = [[0] * (N + 1) for _ in range(N + 1)]
        s, e = 1, 1
        for key in l:
            r, c = check[key]     
            for i in range(s, 1 + r):
                for j in range(e, 1 + c):
                    d[i][j] = nums[i-1][j-1] + max(d[i-1][j], d[i][j-1])
            s, e = r, c
        for i in range(s, 1 + N):
            for j in range(e, 1 + N):
                d[i][j] = nums[i-1][j-1] + max(d[i-1][j], d[i][j-1])        
        print(d[N][N])
    else:
        print(-1)