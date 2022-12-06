input()
s,*q=[*map(int,input().split())]
t=0
for n in q:t+=n*s;s+=n
print(t)