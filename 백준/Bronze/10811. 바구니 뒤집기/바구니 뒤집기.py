g=lambda:map(int, input().split())
N,M=g()
b=[*range(1,1+N)]
for _ in[0]*M:
    i,j=g()
    b=b[:i-1]+[*reversed(b[i-1:j])]+b[j:]
print(*b)