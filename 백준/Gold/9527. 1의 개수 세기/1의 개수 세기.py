def solve(N):
    s = bin(N)[2:]
    k, ans = len(s), 0
    for i in range(k-1, -1, -1):
        if s[k-1-i] == '1':
            ans += d[i] + N + 1 - (1 << i)
            N -= 1 << i
    return ans

d = [0] * 55
for i in range(1, 55):
    d[i] = (d[i-1] << 1) + (1 << (i - 1))
A, B = map(int, input().split())
print(solve(B) - solve(A-1))