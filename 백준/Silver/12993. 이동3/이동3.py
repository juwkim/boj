x,y=map(int,input().split())
a=1
while x or y:
 x,p=divmod(x,3)
 y,q=divmod(y,3)
 if p+q!=1:a=0;break
print(a)