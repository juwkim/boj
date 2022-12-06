K,A=int(input().split()[1]),[*map(int,input().split(','))]
for _ in[0]*K:A=[y-x for x,y in zip(A,A[1:])]
print(*A,sep=',')