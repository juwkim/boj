N, M = map(int, input().split())
a = input()
ans = 1
for _ in range(N-1):
    b = input()
    if all(a[i:] != b[:M-i] for i in range(M)) and all(b[i:] != a[:M-i] for i in range(M)):
        ans = 0
        break    
    a = b
print(ans)