N=len(s:=input())
a,c=N,0
for i in range(N-1):
    if c!=s[i].isupper():a+=1;c^=c!=s[i+1].isupper()
print(a+(c!=s[-1].isupper()))