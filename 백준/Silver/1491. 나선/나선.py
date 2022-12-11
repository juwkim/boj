N, M = map(int, input().split())
p, q = sorted((N, M))
s = (p + 1) >> 1
print(*(s-1,(s,q-s)[p&1])[::1-2*(p&1)*(M<N)])