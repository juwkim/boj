N=int(input())
a,s=map(sorted,zip(*[[*map(int,input().split())]for _ in range(N)]))
print(sum((a[i]-a[i-1]+s[i]-s[i-1])*i*(N-i)for i in range(1,N)))