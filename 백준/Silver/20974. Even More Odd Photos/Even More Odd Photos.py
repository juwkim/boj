input()
a=[0,0]
for c in map(int,input().split()):a[c&1]+=1
e,o=a
t=max(0,(o-e+2)//3)
o-=t*2
print(o+min(o+1,e+t))