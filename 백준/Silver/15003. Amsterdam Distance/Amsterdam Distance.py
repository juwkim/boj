M,N,R=input().split()
ax,ay,bx,by=map(int,input().split())
print((min(1,abs(ax-bx)*3.141592/int(M)-1)*min(ay,by)+max(ay,by))*float(R)/int(N))