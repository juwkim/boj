g = lambda: [*map(int, input().split())]

N, K = g()
s = input()
check = bytearray(N)
ans = 0
for i in range(N):
    if s[i] == 'P':
        for j in range(max(0, i-K), min(N, i + K + 1)):
            if s[j] == 'H' and check[j] == 0:
                ans += 1
                check[j] = 1
                break
print(ans)