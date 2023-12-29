N = int(input())
ans = N - 1
for i in range(2, int(N **.5) + 1):
    if N % i == 0:
        ans = N - max(i, N // i)
        break
print(ans)