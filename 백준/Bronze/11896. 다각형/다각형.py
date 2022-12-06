a,b=map(int,input().split())
a=max(a+a%2,4)
b-=b%2
print(max(0,(b+a)*(b-a+2)//4))