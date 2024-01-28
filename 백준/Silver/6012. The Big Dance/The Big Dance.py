def a(l,r):
 if r==l:return 0
 if r==l+1:return l*r
 d=r-l>>1;return a(l,l+d)+a(l+d+1,r)
print(a(1,int(input())))