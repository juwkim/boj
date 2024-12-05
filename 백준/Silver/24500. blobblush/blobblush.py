N=int(input())
print(*((2,(1<<N.bit_length())-N-1,N),(1,N))[N&N+1==0])