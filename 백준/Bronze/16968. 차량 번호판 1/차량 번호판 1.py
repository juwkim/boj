s,n=input(),{'c':26,'d':10}
t=n[s[0]]
for a,b in zip(s,s[1:]):t*=n[b]-(a==b)
print(t)