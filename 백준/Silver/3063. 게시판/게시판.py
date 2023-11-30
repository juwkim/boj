for _ in range(int(input())):
 a,b,c,d,e,f,g,h=map(int,input().split())
 print((c-a)*(d-b)-max(0,min(c,g)-max(a,e))*max(0,min(d,h)-max(b,f)))