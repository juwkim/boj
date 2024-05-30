input()
a,i=0,1
for c in input():
 if'2'==c:a+=i*(i+1);i+=1
 else:i=1
print(a//2)