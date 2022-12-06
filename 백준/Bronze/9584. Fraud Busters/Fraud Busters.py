c,r,n=input().replace(' ', ''),[],0
for _ in[0]*int(input()):
    k=input()
    if sum(x in'*'+y for x,y in zip(c,k))==len(c):n+=1;r+=[k]
print(n,*r)