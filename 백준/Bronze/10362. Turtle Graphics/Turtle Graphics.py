for i in range(int(input())):
    x,y=map(int,input().split())
    a,d=[[0]*65for _ in[0]*65],0
    a[x][y]+=1
    for s in input():
        if s=='F':
            x+=(d==3)-(d==1)
            y+=(d==0)-(d==2)
            a[x][y]+=1
        else:d=(d+'R L'.index(s)-1)%4
    print(f'Case #{i+1}: {x} {y} {sum(sum(c>1 for c in i)for i in a)}')