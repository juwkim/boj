for _ in[0]*int(input()):
    A,n=map(int,input().split())
    s=''
    while A:
        s+='0123456789abcdef'[A%n]
        A//=n
    print(int(s==s[::-1]))