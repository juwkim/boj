N,a,*H,b=map(int,open(0).read().split())
print(2*(a*a+b*b+2*sum(c*c for c in H)))