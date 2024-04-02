s=[*map(sorted,zip(*[[*map(int,input().split())]for _ in range(int(input()))]))]
t=max(s,key=lambda x:(sum(x),x.count(3),x.count(2)))
print((s.index(t)+1)*(s.count(t)==1),sum(t))