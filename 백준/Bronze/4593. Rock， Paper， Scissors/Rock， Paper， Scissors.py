g=lambda p,q:sum(a+b in'PR RS SP'for a,b in zip(p,q))
while(s:=input())!='E':t=input();print(f'P1: {g(s,t)}\nP2: {g(t,s)}')