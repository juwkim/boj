import re
for _ in range(int(input())):
 l=re.split('[<>]', input())
 print(*l,sep='')
 print(input()[:-3]+l[3]+l[2]+l[1]+l[4])