N=int(input())
print(*range(1,N+N%2,2),*range(N-N%2,0,-2))