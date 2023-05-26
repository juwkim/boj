N=int(input())
s=sorted(map(int,input().split()))
i=max(range(N-1),key=lambda x:s[x+1]-s[x]>>1)
a,b=s[i],s[i+1]
print([-1,(a+b)>>1][b-a>1])