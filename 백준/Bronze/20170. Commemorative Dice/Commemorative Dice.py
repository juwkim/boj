import math,itertools as i
g=lambda:map(int,input().split())
a=sum(x>y for x,y in i.product(g(),g()))
b=math.gcd(a,36)
print(f'{a//b}/{36//b}')