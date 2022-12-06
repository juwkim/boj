a,b,c,d,e,f=zip(*[[*map(int,input().split())]for _ in[0]*int(input())])
a,b,c=map(max,[a,b,c])
d,e,f=map(min,[d,e,f])
print(max(0,(d-a)*(e-b)*(f-c)))