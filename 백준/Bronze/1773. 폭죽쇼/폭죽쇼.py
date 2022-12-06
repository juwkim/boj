N,C=map(int,input().split())
a,t={int(input())for _ in[0]*N},set()
for p in a:t|={*range(p,C+1,p)}
print(len(t))