for _ in range(int(input())):
    a=[*map(int,input().split())]
    print(sum(max(y-2*x,0)for x,y in zip(a,a[1:])))