s=input()
l=len(s)
x=y=1
for i in range(l):x=x*2-(s[i]in'02');y=y*2-(s[i]in'01')
print(l,x-1,y-1)