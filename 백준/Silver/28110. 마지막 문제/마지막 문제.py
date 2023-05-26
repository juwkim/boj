N=int(input())
s=sorted(map(int,input().split()))
a,b=max(zip(s,s[1:]),key=lambda x:x[1]-x[0]>>1)
print([-1,a+b>>1][b-a>1])