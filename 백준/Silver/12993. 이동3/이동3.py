x,y=map(int,input().split())
while x%3+y%3==1:
 x//=3;y//=3
print(+(x+y==0))