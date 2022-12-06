a=[[1]*25,*[[0]*25 for _ in[0]*24]]
for i in range(1,25):
    a[i][0]=1
    for j in range(1,25):a[i][j]=a[i-1][j]+a[i][j-1] 
for i in range(int(input())):R,C=map(int,input().split());print(f'Case #{i+1}: {a[R-1][C-1]}')