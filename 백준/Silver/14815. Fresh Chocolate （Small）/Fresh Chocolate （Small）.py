g=lambda:map(int,input().split())
for i in range(int(input())):
 N,P=g();l=[0]*3
 for n in g():l[n%P]+=1
 a,b,c=l;t=abs(c-b);print(f'Case #{i+1}:',a+t//P+min(b,c)+(t%P!=0))