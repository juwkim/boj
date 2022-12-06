g=lambda:sorted(map(int,input().split()))
print(sum(a>b for a,b in zip(g(),g())))