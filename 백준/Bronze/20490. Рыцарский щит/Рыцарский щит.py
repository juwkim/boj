g=lambda:sorted(map(int,input().split()))
s,t=g(),g()
print(sum(s)+sum(t)-2*min(s[2],t[2]))