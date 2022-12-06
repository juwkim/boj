import sys
a,b,c,d,s=map(int,sys.stdin.read().split())
A=s//(x:=(a+b))*(a-b)+min((y:=s%(x)),2*a-y)
B=s//(m:=(c+d))*(c-d)+min((n:=s%(m)),2*c-n)
print('Tied Nikky Byron'.split()[(A>B)-(A<B)])