N, P = map(int, input().split())
s = 1
for i in range(1, N+1):
    s = s*i % P
print(s)