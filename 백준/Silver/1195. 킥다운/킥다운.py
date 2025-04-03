def f(s,t):
 i=0
 while i<len(s)and any(s[i+j]+t[j]=="22"for j in range(min(len(s)-i,len(t)))):i+=1
 return max(len(s),i+len(t))
a,b=input(),input()
print(min(f(a,b),f(b,a)))