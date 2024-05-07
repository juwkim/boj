import math
a,b,c=map(int,input().split())
print((c*c-a-b,math.isqrt(a+b))[c==0])