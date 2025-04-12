a,b,m=1,0,10**9+7
for _ in range(int(input())):a,b=2*(a+b)%m,a
print((a+b)%m)