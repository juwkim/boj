N,K=map(int,input().split())
for _ in range(K):
    S,T,R=map(int,input().split())
    print(-(N//-S)-(((N//-S)//T)+1)*R)