for i in range(int(input())):
    R,A,B=map(int,input().split())
    ans=0
    while R:ans+=R*R+R*R*A*A;R=R*A//B
    print(f'Case #{i+1}:',ans*3.14159)