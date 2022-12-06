n=[*map(int,input().split())]
g=lambda x:(n[x+2]-n[x])**2+(n[x+3]-n[x+1])**2
print(max(g(0),g(4))**.5)