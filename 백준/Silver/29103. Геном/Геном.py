x,y,z,k=map(int,input().split())
print([x-y,y-x][k&1])