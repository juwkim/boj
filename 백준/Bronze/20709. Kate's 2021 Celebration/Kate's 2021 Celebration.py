f=0
for _,a,i in sorted([input().split()+[i]for i in range(1,1+int(input()))],key=lambda x:int(x[0])):
    if '0'in a and '1'in a and a.count('2')>1:f=i;break
print(f)