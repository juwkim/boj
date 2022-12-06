a,b,c=1,0,[]
for i in range(491):
    a,b=b,a+b
    c+=[a]
while(h:=int(input()))>0:print(f'Hour {h}: {c[h]} cow(s) affected')