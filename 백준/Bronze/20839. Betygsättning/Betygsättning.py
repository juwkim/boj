g=lambda:map(int,input().split())
A,C,E=g()
x,y,z=g()
print("EDCBA"[(2*y>=C)+((y>=C)and((x>=A)+(2*x>=A)+1))])