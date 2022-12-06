N=int(input())
a="@"*N
s=(a*5+"\n")*N
print(s+(a+" "*3*N+a+"\n")*3*N+s)