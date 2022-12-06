a,b,c,d=sorted(map(int,input().split()))
print(min(abs(d-a-b-c),abs(d+a-b-c)))