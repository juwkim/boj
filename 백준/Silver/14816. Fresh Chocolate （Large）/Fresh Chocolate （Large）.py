g=lambda:map(int,input().split())
for i in range(int(input())):
 N,P=g();l=[0]*4
 for n in g():l[n%P]+=1
 a,b,c,d=l
 if P==4:c,d=d,c
 print(f'Case #{i+1}:',a+(t:=abs(c-b))//P+min(b,c)+d//2+[d&1,1,1,1+(d&1)][t%P])