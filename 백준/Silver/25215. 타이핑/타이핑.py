N=len(s:=input())
a,c=N,0
for i in range(N-1):p=(s[i]<'[')^c;a+=p;c^=(c^(s[i+1]<'['))&p
print(a+(c^(s[-1]<'[')))