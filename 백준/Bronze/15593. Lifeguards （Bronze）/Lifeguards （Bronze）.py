t,g=[0]*1000,[[*map(int,input().split())] for _ in[0]*int(input())]
for a,b in g:
    for i in range(a,b):t[i]+=1   
print(max(1000-t[a:b].count(1)for a,b in g)-t.count(0))