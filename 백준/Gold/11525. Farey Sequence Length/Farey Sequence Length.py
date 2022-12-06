to = {1: 2}
for n in range(2,10001):
    s,p=n,n
    for t in range(2, int(n**.5)+1):
        if not n%t:
            p-=p//t
            while not n%t:
                n//=t
    if n>1:p-=p//n
    to[s]=p+to[s-1]
for _ in[0]*int(input()):
    k,n=map(int,input().split())
    print(k,to[n])