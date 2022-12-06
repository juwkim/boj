m,n=map(int,input().split())
q=''
while m:q=hex(m%n)[2].upper()+q;m//=n
print(q or 0)