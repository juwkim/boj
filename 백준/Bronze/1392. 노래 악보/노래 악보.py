I,A=input,int
N,Q=map(A,I().split())
t,s=[],-1
for _ in[0]*N:t+=[s:=s+A(I())]
for _ in[0]*Q:
    i,p=0,A(I())
    while(t[i]<p):i+=1
    print(i+1)