g=lambda p,a,b:sum((int(s[i])-int(p[i]))**2 for i in range(a,b))
s,n,*l=open(0)
print(max(sorted(l),key=lambda p:g(p,0,4)*g(p,4,6)*g(p,6,8)))