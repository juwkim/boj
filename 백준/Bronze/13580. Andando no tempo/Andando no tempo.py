a,b,c=sorted(map(int,input().split()))
print("NS"[(a-b)*(b-c)*(a+b-c)==0])