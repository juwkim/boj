g=lambda:[*map(int,input().split())]
s,t=g(),g()
print(sum(s)+sum(t)-2*min(max(s),max(t)))