a,b,c,d=map(int,input().split())
x,y=a*b,c*d
print('EMP'[(x>y)-(x<y)])