n=int(input())
print(sum(max(i+2-(n-i)//2,0)for i in range((n-1)//2)))