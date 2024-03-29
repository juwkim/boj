n=int(input())
a=[[*map(int,input().split())]for _ in' '*n]
print(min(range(n),key=lambda i:a[i][0]/(a[i][2]-a[i][1]))+1)