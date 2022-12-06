g = lambda: [*map(int, input().split())]


ans = 'Y'
Map = [[0] * 10 for _ in range(10)]
for _ in range(int(input())):
    D, L, R, C = g()

    if D:
        if R + L - 1 > 10:
            ans = 'N'
            break
        for i in range(R-1, R+L-1):
            if Map[i][C-1]:
                ans = 'N'
                break
            Map[i][C-1] = 1        
    else:
        if C + L - 1 > 10:
            ans = 'N'
            break
        for i in range(C-1, C+L-1):
            if Map[R-1][i]:
                ans = 'N'
                break
            Map[R-1][i] = 1    
print(ans)