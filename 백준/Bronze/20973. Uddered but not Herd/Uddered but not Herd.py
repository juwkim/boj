a,s=input(),input()
print(1+sum(a.index(x)>=a.index(y)for x,y in zip(s,s[1:])))