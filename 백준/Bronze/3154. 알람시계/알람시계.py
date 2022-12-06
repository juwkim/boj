def e(h,m):
    k=[*map(lambda x:(x-1)%11,[h//10,h%10,m//10,m%10])]
    return sum(abs(a//3-b//3)+abs(a%3-b%3)for a,b in zip(k,k[1:])),h,m
g=lambda x:[e(i,m+x)for i in range(h,100,24)]
h,m=map(int,input().split(':'))
_,a,b=min(g(0)+g(60))
print('%02d:%02d'%(a,b))