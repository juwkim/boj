import sys
I=sys.stdin.readline
for _ in[0]*int(I()):a,b,c=sorted(map(int,I().split()));print((a+b)**2+c*c)