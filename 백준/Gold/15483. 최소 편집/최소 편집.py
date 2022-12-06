A,B,r=input(),input(),range
p=[*r(1001)]
for i in r(len(A)):
 c=[i+1]
 for j in r(len(B)):
  if A[i]==B[j]:c+=[p[j]]
  else:c+=[1+min(c[-1],p[j],p[j+1])]
 p=c
print(c[-1])