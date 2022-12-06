g=lambda x:eval('*'.join(x))
M=int(input())
a,b,c=zip(*[input().split()for _ in' '*M])
print(c.count('1')%2,int(g(b)/g(a)))