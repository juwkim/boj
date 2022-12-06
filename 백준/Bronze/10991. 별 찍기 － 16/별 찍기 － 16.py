N=int(input())
[print(('* '*i).rjust(N+i))for i in range(1,N+1)]