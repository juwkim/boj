N = int(input())
ans, num = 0, 2
while N:
    ans += num * (N - N // 2)
    N >>= 1
    num <<= 1
print(ans)