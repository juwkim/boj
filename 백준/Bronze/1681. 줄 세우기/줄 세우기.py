N,L=input().split()
N,i=int(N),0
while N:
    i+=1
    N-=(L not in str(i))
print(i)