N,P=map(int,input().split())
r=(N-P)//2%P
print(2*r*(N%P!=0))