l=[[*map(int,input().split())]for _ in range(int(input()))]
print(max(2*max(l)[0],*map(sum,l)))