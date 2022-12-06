n=int(input())
for i in range(n):print(*range(1+i*n,1+(i+1)*n)[::(-1)**i])