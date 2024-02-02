s=len(str(n:=int(input())))
print(s*(n//10+1)+(1-10**(s-1))//9+(n>1)*(n%10!=0)*s)