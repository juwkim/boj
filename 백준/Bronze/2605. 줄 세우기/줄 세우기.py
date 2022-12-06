n,k,o=[],int(input()),[*map(int,input().split())]
for i in range(k):n.insert(i-o[i],i+1)
print(*n)