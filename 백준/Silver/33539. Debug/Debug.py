n=int(input())
print(("no","yes")[n>1 and all(n%i for i in range(2,int(n**.5)+1))])