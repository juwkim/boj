for _ in[0]*int(input()):
    n=[*map(int,input().split())][1:]
    i=0
    while n[i+1]-n[i]==1:i+=1
    print(i+2)