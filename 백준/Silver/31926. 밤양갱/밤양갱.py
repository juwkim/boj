N = int(input())
ans = 9
while N:
    N >>= 1
    ans += 1
print(ans)