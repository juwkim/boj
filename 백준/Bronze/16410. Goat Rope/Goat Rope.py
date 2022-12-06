a,b,c,d,e,f=map(int,input().split())
print((max(0,a-e,c-a)**2+max(0,b-f,d-b)**2)**.5)