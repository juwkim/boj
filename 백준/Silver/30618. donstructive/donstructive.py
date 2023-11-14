N=int(input())
print(*range(1,N+1,2),*range(N-N%2,0,-2))