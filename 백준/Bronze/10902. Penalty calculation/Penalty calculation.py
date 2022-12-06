t,s=zip(*[[*map(int,input().split())]for _ in[0]*int(input())])
print(t[(f:=s.index(max(s)))]+20*f if max(s) else 0) 