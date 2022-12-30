N = int(input())
A = sorted(int(input()) for _ in range(N))
B = sorted(int(input()) for _ in range(N))
ans = 0
for a, b in zip(A, B):
    ans += abs(a - b)
print(ans)