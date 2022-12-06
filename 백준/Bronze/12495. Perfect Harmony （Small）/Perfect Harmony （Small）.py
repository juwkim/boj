I=input
g=lambda:map(int,I().split())
for j in range(int(I())):
    N,L,H=g()
    x,f=[*g()],0
    for i in range(L,H+1):
        if all(not(i%p and p%i)for p in x):f=1;break
    print(f'Case #{j+1}: {["NO",i][f]}')